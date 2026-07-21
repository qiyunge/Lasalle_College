# Model artifacts

The application expects these runtime artifacts in this directory:

- `mlp_classifier.joblib`: best classifier produced by `face-train`
- `training_history.json`: hyperparameter search and validation results
- `evaluation_report.json`: independent test-set results from `face-evaluate`
- `face_detection_yunet_2023mar.onnx`: YuNet detector weights
- `yolov8n-face.pt`: optional YOLO face detector weights
- `haarcascade_frontalface_default.xml`: Haar cascade detector

The current `mlp_classifier.joblib` is only an empty placeholder. Run training before
starting recognition:

```powershell
face-train --validation-dir data/processed/validation --search random
```

Model files must only be loaded from a trusted source because Joblib uses Python
pickle internally.
