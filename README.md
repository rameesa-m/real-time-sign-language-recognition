# Real-Time Sign Language Recognition System

A real-time system that detects hand gestures from a webcam and converts them into speech using Computer Vision and Machine Learning.

---

## What It Does

- Detects hand gestures through webcam
- Recognizes A–Z alphabets and common words (Hello, Thank You, Yes, No, I Love You)
- Speaks out the recognized gesture using text-to-speech

---

## Tech Used

- **Python** – Programming language
- **OpenCV** – Webcam and video processing
- **MediaPipe** – Hand landmark detection (21 points)
- **Scikit-learn** – Random Forest classifier
- **NumPy** – Data processing
- **pyttsx3** – Text-to-speech

---

## How to Install

```bash
git clone https://github.com/your-username/real-time-sign-language-recognition.git
cd real-time-sign-language-recognition
pip install opencv-python mediapipe scikit-learn numpy pyttsx3
```

---

## How to Run

Run these scripts one by one:

```bash
# 1. Collect gesture images
python collect_images.py

# 2. Create the dataset
python create_dataset.py

# 3. Train the model
python train_classifier.py

# 4. Run the app
python app.py        # without voice
python sound_app.py  # with voice
```

> Press **Q** to quit the webcam window.

---

## How It Works

```
Webcam → Hand Detection → Feature Extraction → Normalization → Random Forest → Prediction → Speech
```

1. Webcam captures hand gesture
2. MediaPipe detects 21 hand landmarks (x, y coordinates)
3. Coordinates are normalized for position invariance
4. Random Forest model predicts the gesture
5. Prediction is spoken aloud

---

## Model Details

| Detail | Value |
|---|---|
| Model | Random Forest |
| Input | 42 features (21 landmarks × x, y) |
| Train/Test Split | 80% / 20% |
| Classes | A–Z + 5 common words |

---

## Dataset

The dataset is not included. Use `collect_images.py` to generate your own. Collect at least **100 images per gesture** for good accuracy.

---

## Applications

- Assistive communication for speech-impaired individuals
- Gesture-based human-computer interaction
- Sign language learning tools

---

## Author

**Rameesa M** — MSc Data Analytics

---

## License

For academic and educational use only.
