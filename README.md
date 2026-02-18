# Real-Time Sign Language Recognition System

## Overview

This project presents a real-time Sign Language Recognition system built using MediaPipe hand landmark detection and Machine Learning. The system captures live video input, extracts structured hand landmark features, classifies gestures using a Random Forest model, and converts predictions into speech output.

The solution demonstrates the practical integration of Computer Vision and Machine Learning for assistive technology applications, particularly for supporting speech-impaired communication.

---

## Key Features

- Real-time gesture recognition using webcam input
- Hand landmark detection with MediaPipe (21 keypoints)
- Feature normalization for position invariance
- Random Forest-based gesture classification
- Support for A–Z alphabets
- Support for common words (Hello, Thank You, Yes, No, I Love You)
- Text-to-Speech output using pyttsx3
- Modular and scalable ML pipeline

---

## Technology Stack

- **Python** – Core programming language  
- **OpenCV** – Video capture and visualization  
- **MediaPipe** – Hand landmark detection  
- **Scikit-learn** – Machine Learning model training  
- **NumPy** – Numerical processing  
- **pyttsx3** – Speech synthesis  

---

## System Workflow

1. Capture hand gesture images through webcam.
2. Detect 21 hand landmark coordinates using MediaPipe.
3. Normalize extracted landmark features.
4. Train a Random Forest classifier using labeled data.
5. Perform real-time gesture prediction.
6. Convert predicted output into speech.

---

## System Architecture Diagram

## 🎨 System Workflow

```mermaid
flowchart LR
    A[📷 Webcam Input] --> B[✋ Hand Landmark Detection<br/>(MediaPipe – 21 Keypoints)]
    B --> C[📊 Feature Extraction<br/>(x, y Coordinates)]
    C --> D[⚙ Feature Normalization<br/>(Position Invariant)]
    D --> E[🌲 Random Forest Classifier]
    E --> F[🔤 Gesture Prediction]
    F --> G[🔊 Text-to-Speech Output]

    style A fill:#4CAF50,color:#ffffff,stroke:#2E7D32,stroke-width:2px
    style B fill:#FF9800,color:#ffffff,stroke:#E65100,stroke-width:2px
    style C fill:#2196F3,color:#ffffff,stroke:#0D47A1,stroke-width:2px
    style D fill:#9C27B0,color:#ffffff,stroke:#4A148C,stroke-width:2px
    style E fill:#3F51B5,color:#ffffff,stroke:#1A237E,stroke-width:2px
    style F fill:#E91E63,color:#ffffff,stroke:#880E4F,stroke-width:2px
    style G fill:#009688,color:#ffffff,stroke:#004D40,stroke-width:2px
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/real-time-sign-language-recognition.git
cd real-time-sign-language-recognition
```

### 2. Install Dependencies

```bash
pip install opencv-python mediapipe scikit-learn numpy pyttsx3
```

---

## Usage

### Step 1 – Collect Dataset
```bash
python data_collection.py
```

### Step 2 – Extract Features
```bash
python feature_extraction.py
```

### Step 3 – Train the Model
```bash
python train_model.py
```

### Step 4 – Run Real-Time Prediction
```bash
python predict_with_voice.py
```

Press `Q` to exit the webcam window.

---

## Model Information

- **Model Type:** Random Forest Classifier  
- **Input Features:** Normalized hand landmark coordinates  
- **Train-Test Split:** 80-20  
- **Evaluation Metric:** Accuracy Score  

Random Forest is selected due to its strong performance on structured feature data, low computational complexity, and robustness without requiring deep learning infrastructure.

---

## Dataset Note

The dataset is not included in this repository due to size limitations. Users can generate their own dataset using the provided data collection script.

---

## Applications

- Assistive communication systems  
- Human-computer interaction  
- Gesture-controlled interfaces  
- Educational and research purposes  

---

## Author

Rameesa M  
MSc Data Analytics  

---

## License

This project is developed for academic and educational purposes.
