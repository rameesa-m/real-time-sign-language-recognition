# Real-Time Sign Language Recognition System

## Project Overview

This project implements a real-time Sign Language Recognition system using MediaPipe hand landmarks and Machine Learning. The system captures live video from a webcam, detects hand gestures, classifies them using a trained Random Forest model, and converts predictions into speech.

The project demonstrates the practical integration of Computer Vision and Machine Learning for assistive technology applications.

---

## Features

- Real-time webcam-based gesture detection
- Hand landmark extraction using MediaPipe (21 keypoints)
- Random Forest classification model
- Supports A–Z alphabets
- Supports common words (Hello, Thank You, Yes, No, I Love You)
- Text-to-Speech output using pyttsx3
- End-to-end pipeline: Data Collection → Feature Extraction → Training → Prediction

---

## Technologies Used

- Python  
- OpenCV  
- MediaPipe  
- Scikit-learn  
- NumPy  
- pyttsx3  

---

## System Workflow

1. Capture images using webcam.
2. Extract 21 hand landmark coordinates using MediaPipe.
3. Normalize landmark features.
4. Train a Random Forest classifier.
5. Predict gestures in real time.
6. Convert predicted text into speech.

---
## System Workflow Diagram

```
+------------------+
|   Webcam Input   |
| (Live Video Feed)|
+------------------+
          |
          v
+--------------------------+
|  Hand Detection          |
|  (MediaPipe - 21 Points) |
+--------------------------+
          |
          v
+--------------------------+
|  Feature Extraction      |
|  (x, y Coordinates)      |
+--------------------------+
          |
          v
+--------------------------+
|  Feature Normalization   |
|  (Position Invariant)    |
+--------------------------+
          |
          v
+--------------------------+
|  Random Forest Model     |
|  (Gesture Classification)|
+--------------------------+
          |
          v
+--------------------------+
|  Prediction Output       |
|  (Text Display)          |
+--------------------------+
          |
          v
+--------------------------+
|  Text-to-Speech Engine   |
|  (Audio Output)          |
+--------------------------+
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/real-time-sign-language-recognition.git
cd real-time-sign-language-recognition
```

### 2. Install Required Libraries

```bash
pip install opencv-python mediapipe scikit-learn numpy pyttsx3
```

---

## How to Run

Step 1: Collect Dataset  
```bash
python data_collection.py
```

Step 2: Extract Features  
```bash
python feature_extraction.py
```

Step 3: Train Model  
```bash
python train_model.py
```

Step 4: Run Real-Time Prediction  
```bash
python predict_with_voice.py
```

Press `Q` to exit the webcam window.

---

## Model Details

- Model: Random Forest Classifier  
- Input: Normalized hand landmark coordinates  
- Train-Test Split: 80-20  
- Evaluation Metric: Accuracy Score  

Random Forest is used because the system works with structured landmark coordinate data instead of raw image data, making traditional machine learning efficient and suitable.

---

## Applications

- Assistive technology for speech-impaired individuals  
- Gesture-based human-computer interaction  
- Educational tools  

---

## Author

Rameesa M  
MSc Data Analytics  

---

## License

This project is developed for academic and educational purposes.
