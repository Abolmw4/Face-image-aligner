# 🖼️ FastAPI Face Alignment Service

A lightweight **FastAPI-based API** for detecting, aligning, and returning faces in images.  
Supports **single or multiple images** in **Base64 format**.  
Built with OpenCV, NumPy, and a clean serialization/deserialization pipeline.

---

## ✨ Features
- 📸 **Face Alignment** – Processes unaligned faces and returns aligned results.
- 📦 **Base64 Serialization** – Send/receive images as Base64 strings over JSON.
- ⚡ **FastAPI Backend** – Async API with automatic OpenAPI docs.
- 🐳 **Docker Ready** – Easy to run anywhere.

---

## 📂 Project Structure
````
Face-image-aligner/
    ├── config/
    │   └── config.json # API configuration (host, port, dataset path, model path)
    ├── data_model/
    │   └── request_body.py # Pydantic model for API requests
    ├── dataset/ # Folder for input images
    ├── facealigner/
    │ ├── init.py
    │ └── facealignment.py # Face alignment logic
    ├── models/
    │ └── shape_predictor_68_face_landmarks.dat # Pretrained facial landmarks model
    ├── tests/
    │ └── test_facealignment.py # Test cases
    ├── utils/
    │ ├── endpoints.py # FastAPI routes
    │ └── util.py # Serialization/deserialization helpers
    ├── main.py # FastAPI entry point
    ├── Dockerfile
    ├── docker-compose.yaml
    ├── requirements.txt
    └── README.md
````
---

## 🧰 Prerequisites
- Python 3.13
- dlib (with CUDA support recommended)
- OpenCV
- Docker (optional)

## ⚙️ Installation
```bash
# Clone repository
git https://github.com/Abolmw4/Face-image-aligner.git
cd face_aligner

# Install dependencies
pip install -r requirement.txt

# Download model (if not included)
wget https://github.com/ageitgey/face_recognition_models/blob/master/face_recognition_models/models/shape_predictor_68_face_landmarks.dat
mv shape_predictor_68_face_landmarks.dat facealigner/models/
```
----
## 🚀 Usage

### 💻 Command Line Interface
```bash
python main.py -i input.jpg -o aligned.jpg --landmarks
```

---

## 🐳 Docker Deployment
```bash
# Build and run
docker-compose up --build

# Test service
curl -X POST -F "image=@test.jpg" http://localhost:5000/align > result.jpg
```
---



## ⚙️ Configuration

```json
{
    "dataset_dir":"/home/app/alignment/dataset",
    "result_path":"/home/app/alignment/dataset/aligned_result",
    "ip":"0.0.0.0",
    "port":8081,
    "model_path":"/home/app/alignment/models/shape_predictor_68_face_landmarks.dat"
}
```

---
