const API_BASE = document.body.dataset.apiBase.replace(/\/$/, "");

async function loadModelInformation() {
  const ready = document.querySelector("#model-ready");
  const error = document.querySelector("#model-error");
  try {
    const response = await fetch(`${API_BASE}/api/v1/model`);
    if (!response.ok) throw new Error(response.statusText);
    const model = await response.json();
    ready.textContent = model.ready ? "Ready" : "Unavailable";
    ready.className = model.ready ? "ready" : "warning";
    document.querySelector("#model-detector").textContent = model.detector;
    document.querySelector("#model-threshold").textContent = `${Math.round(model.threshold * 100)}%`;
    document.querySelector("#model-class-count").textContent = model.classes.length;
    document.querySelector("#model-path").textContent = model.path;
    document.querySelector("#model-classes").innerHTML = model.classes.length
      ? model.classes.map((label) => `<span>${escapeHtml(label)}</span>`).join("")
      : "<p>No classifier is currently loaded.</p>";
    if (model.detail) {
      error.textContent = model.detail;
      error.hidden = false;
    }
  } catch (reason) {
    ready.textContent = "API unavailable";
    ready.className = "warning";
    error.textContent = reason.message;
    error.hidden = false;
  }
}

function escapeHtml(value) {
  const element = document.createElement("span");
  element.textContent = value;
  return element.innerHTML;
}

loadModelInformation();
