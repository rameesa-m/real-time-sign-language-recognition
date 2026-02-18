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

```
Webcam Input
      ↓
Hand Detection (MediaPipe – 21 Landmarks)
      ↓
Feature Extraction (x, y Coordinates)
      ↓
Feature Normalization
      ↓
Random Forest Classifier
      ↓
Gesture Prediction
      ↓
Text-to-Speech Output
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

Step 1 – Collect Dataset
python collect_images.py

Step 2 – Create Dataset File
python create_dataset.py

Step 3 – Train the Model
python train_classifier.py

Step 4 – Run Real-Time Recognition

Without voice output:

python app.py


With voice output:

python sound_app.py


Press Q to exit the webcam window.

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
