**Real-Time Sign Language Recognition System**
**Overview**

This project presents a **Real-Time Sign Language Recognition System** using **Computer Vision** and **Machine Learning** techniques.  
The system captures live webcam input, detects hand landmarks using **MediaPipe**, extracts normalized spatial features, and classifies gestures with a **Random Forest** model.  

Predicted gestures are displayed on-screen and can be converted into **speech output**, enabling assistive communication for speech-impaired individuals.  

 **Key Features**
- Real-time gesture recognition via webcam  
- Detection of **21 hand landmarks** using MediaPipe  
- **Feature normalization** for translation invariance  
- **Random Forest** based gesture classification  
- Recognition of **A–Z alphabets**  
- Recognition of common words:
  - Hello  
  - Thank You  
  - Yes / No  
  - I Love You  
- Optional **Text-to-Speech** output using pyttsx3  
- Modular and **scalable ML pipeline**


**Technology Stack**
Technology	Purpose
Python	Core programming language
OpenCV	Video capture and visualization
MediaPipe	Hand landmark detection
Scikit-learn	Machine Learning model training
NumPy	Numerical computations
pyttsx3	Text-to-Speech conversion

**System Workflow**

1. Capture live video stream from webcam  
2. Detect hand using MediaPipe and extract **21 landmark coordinates**  
3. Normalize features for position invariance  
4. Train a **Random Forest** classifier using labeled gesture data  
5. Perform **real-time gesture prediction**  
6. Convert predicted output into speech (optional) 

**System Architecture**
        Webcam Input
              ↓
  Hand Detection (MediaPipe)
       21 Landmarks
              ↓
   Feature Extraction (x, y)
              ↓
    Feature Normalization
              ↓
  Random Forest Classifier
              ↓
      Gesture Prediction
              ↓
   Text Display / Speech Output

**Installation**
**Clone the Repository**
git clone https://github.com/your-username/real-time-sign-language-recognition.git
cd real-time-sign-language-recognition

**Install Required Dependencies**
pip install opencv-python mediapipe scikit-learn numpy pyttsx3

**Usage**
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

**Model Details**

Model Type: Random Forest Classifier

Input Features: Normalized (x, y) hand landmark coordinates

Train-Test Split: 80:20

Evaluation Metric: Accuracy Score

**Why Random Forest?**

Random Forest was selected because:

It performs well on structured numerical feature data

It requires minimal hyperparameter tuning

It is computationally efficient

It avoids the need for GPU-intensive deep learning models

**Dataset Information**

The dataset is not included in this repository due to size constraints.

Users can generate their own dataset using the provided data collection script. The system is designed to support custom gesture expansion and scalability.

**Applications**

Assistive communication systems

Human-Computer Interaction (HCI)

Gesture-based control systems

Educational and academic research

Accessibility-focused technology solutions

**Author**

Rameesa M
MSc Data Analytics

**License**

This project is developed for academic and educational purposes.
It may be extended for research and non-commercial applications.
