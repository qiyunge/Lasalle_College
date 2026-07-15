import cv2
import os
from pathlib import Path

from ultralytics import YOLO

cap = cv2.VideoCapture(0)

print("Press 'q' to quit the webcam capture.")
if  not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# YUNet model
model_path = "Final_Projects/face-recognition-app/models/face_detection_yunet_2023mar.onnx"
print("cwd:", os.getcwd())
print("model_path:", Path(model_path).resolve())
detector = cv2.FaceDetectorYN.create(model_path, "",
                                      (320, 320),
                                      score_threshold=0.7,
                                      nms_threshold=0.4,
                                      top_k=5000,)
print("cwd:", os.getcwd())
print("model_path:", Path(model_path).resolve())

# Haar Cascade classifier
cascade_path = (
    r"C:\Users\devuser\.conda\envs\face-recognition-app"
    r"\Library\etc\haarcascades"
    r"\haarcascade_frontalface_default.xml"
)
face_cascade = cv2.CascadeClassifier(cascade_path)

# YOLov8 model
model_yolov8_path = "Final_Projects/face-recognition-app/models/yolov8n-face.pt"
YOLO_model = YOLO(model_yolov8_path)



while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # cv2.imshow("Webcam", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 1. detect by Haar Cascade classifier
    # Detect faces using the Haar Cascade classifier
    # faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 2. Detect faces using the YUNet model
    # h,w = frame.shape[:2]
    # detector.setInputSize((w, h))
    # _, faces = detector.detect(frame)

    # if faces is not None:
    #     for face in faces:
    #         x, y, w, h = face[:4].astype(int)
    #         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #         cv2.putText(frame, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # 3. Detect faces using the YOLOv8 model
    CONFIDENCE_THRESHOLD = 0.5  # Set your desired confidence threshold here

    results = YOLO_model.predict(
        source=frame,
        conf = CONFIDENCE_THRESHOLD,
        verbose=False,
        device="cuda"  # Use "cuda" if you have a compatible GPU
        )
    result = results[0]  # Get the first result (assuming only one image is processed)
    if result.boxes is not None:
        for box in result.boxes:
            x1, y1, x2, y2 = (box.xyxy[0].cpu().numpy()).astype(int)

            confidence = float(box.conf[0].cpu())
            height ,width = frame.shape[:2]
            x1 = max(0, min(x1, width - 1))
            y1 = max(0, min(y1, height - 1))

            x2 = max(0, min(x2, width - 1))
            y2 = max(0, min(y2, height - 1))

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"Face: {confidence:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2) 
            
    cv2.imshow("Webcam", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()