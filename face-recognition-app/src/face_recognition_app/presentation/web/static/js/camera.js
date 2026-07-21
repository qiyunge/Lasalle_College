const API_BASE = document.body.dataset.apiBase.replace(/\/$/, "");
const video = document.querySelector("#video");
const overlay = document.querySelector("#overlay");
const capture = document.querySelector("#capture");
const startButton = document.querySelector("#start");
const stopButton = document.querySelector("#stop");
const statusText = document.querySelector("#status");
const emptyState = document.querySelector("#empty-state");
const faceCount = document.querySelector("#face-count");

let stream = null;
let timer = null;
let requestPending = false;
let recognitionReady = false;

async function loadModelStatus() {
  try {
    const response = await fetch(`${API_BASE}/api/v1/model`);
    const model = await response.json();
    recognitionReady = model.ready;
    document.querySelector("#model-status").textContent = model.ready ? "Ready" : "Unavailable";
    document.querySelector("#classes").textContent = model.classes.join(", ") || "No model loaded";
    statusText.textContent = model.ready ? "Inference service ready" : "Preview available — model not ready";
    startButton.disabled = false;
  } catch (error) {
    statusText.textContent = "Preview available — API unreachable";
    startButton.disabled = false;
  }
}

async function startCamera() {
  try {
    stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" }, audio: false });
    video.srcObject = stream;
    await video.play();
    emptyState.hidden = true;
    startButton.disabled = true;
    stopButton.disabled = false;
    statusText.textContent = recognitionReady ? "Recognition active" : "Camera preview only — model unavailable";
    timer = window.setInterval(sendFrame, 350);
  } catch (error) {
    statusText.textContent = `Camera unavailable: ${error.message}`;
  }
}

function stopCamera() {
  window.clearInterval(timer);
  timer = null;
  stream?.getTracks().forEach((track) => track.stop());
  stream = null;
  video.srcObject = null;
  overlay.getContext("2d").clearRect(0, 0, overlay.width, overlay.height);
  emptyState.hidden = false;
  startButton.disabled = false;
  stopButton.disabled = true;
  faceCount.textContent = "0";
  statusText.textContent = "Camera stopped";
}

async function sendFrame() {
  if (requestPending || !video.videoWidth || !recognitionReady) return;
  requestPending = true;
  capture.width = video.videoWidth;
  capture.height = video.videoHeight;
  capture.getContext("2d").drawImage(video, 0, 0);
  const blob = await new Promise((resolve) => capture.toBlob(resolve, "image/jpeg", 0.78));
  try {
    const response = await fetch(`${API_BASE}/api/v1/recognize`, {
      method: "POST",
      headers: { "Content-Type": "image/jpeg" },
      body: blob,
    });
    if (!response.ok) throw new Error((await response.json()).detail || response.statusText);
    drawFaces(await response.json());
  } catch (error) {
    statusText.textContent = `Recognition failed: ${error.message}`;
  } finally {
    requestPending = false;
  }
}

function drawFaces(result) {
  overlay.width = video.clientWidth;
  overlay.height = video.clientHeight;
  const context = overlay.getContext("2d");
  context.clearRect(0, 0, overlay.width, overlay.height);
  const scaleX = overlay.width / result.width;
  const scaleY = overlay.height / result.height;
  context.font = "600 15px system-ui";
  result.faces.forEach((face) => {
    const [x1, y1, x2, y2] = face.bbox;
    const x = x1 * scaleX;
    const y = y1 * scaleY;
    const width = (x2 - x1) * scaleX;
    const height = (y2 - y1) * scaleY;
    const label = `${face.label} ${(face.confidence * 100).toFixed(0)}%`;
    context.strokeStyle = "#5eead4";
    context.lineWidth = 3;
    context.strokeRect(x, y, width, height);
    context.fillStyle = "#5eead4";
    context.fillRect(x, Math.max(0, y - 25), context.measureText(label).width + 14, 25);
    context.fillStyle = "#06221f";
    context.fillText(label, x + 7, Math.max(18, y - 7));
  });
  faceCount.textContent = String(result.faces.length);
}

startButton.addEventListener("click", startCamera);
stopButton.addEventListener("click", stopCamera);
window.addEventListener("beforeunload", stopCamera);
loadModelStatus();
