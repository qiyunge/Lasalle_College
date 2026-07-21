# Face Recognition App

An end-to-end, multi-class face recognition project with dataset capture,
preprocessing, hyperparameter search, evaluation, real-time OpenCV inference, and a
FastAPI browser client.

## Install

```powershell
python -m pip install -e ".[dev]"
```

Install the optional YOLO detector with:

```powershell
python -m pip install -e ".[yolo]"
```

## Pipeline

Class labels come from directory names. Each person must have a separate folder
under `data/raw/`.

```powershell
face-preprocess --input-dir data/raw --output-dir data/preprocessed
face-split --input-dir data/preprocessed --output-dir data/processed
face-train --validation-dir data/processed/validation --search random
face-evaluate --test-dir data/processed/test
face-recognize --detector yunet --camera 0
```

## Web application

The Web UI and API are separate modules served by one FastAPI process. Start the
application after producing a non-empty classifier model:

```powershell
face-app --host 0.0.0.0 --port 8000
```

Open the application locally:

```text
http://127.0.0.1:8000
```

The browser captures a compressed JPEG frame about three times per second and
sends it to the same-origin API. Camera access requires localhost or HTTPS.

The Jinja2 web client uses a shared `base.html` layout. Presentation code and
assets are packaged under `face_recognition_app.presentation`. Only its `static/`
directory is publicly mounted; `templates/` cannot be requested as static files.

Presentation-layer structure:

```text
src/face_recognition_app/
├── app.py
├── presentation/
│   ├── api/
│   │   ├── dependencies.py
│   │   ├── schemas.py
│   │   └── routers/
│   └── web/
│       ├── routers/
│       ├── templates/
│       └── static/
└── inference/
    └── service.py
```

API endpoints:

- `GET /api/v1/health`: readiness and model-loading errors
- `GET /api/v1/model`: detector, threshold, and known classes
- `POST /api/v1/recognize`: raw JPEG request body and JSON face results
- `GET /api/docs`: interactive OpenAPI documentation

Example recognition response:

```json
{
  "width": 1280,
  "height": 720,
  "faces": [
    {
      "label": "Ada",
      "confidence": 0.93,
      "bbox": [120, 80, 260, 250]
    }
  ]
}
```

Joblib model files use Python pickle internally. Only deploy model files produced
by a trusted training environment.
