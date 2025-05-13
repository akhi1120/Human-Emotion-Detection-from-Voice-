# Speech Emotion Detection from Voice

This project is a machine learning-based Speech Emotion Recognition (SER) system built with Python. It classifies human emotions (like happy, sad, angry, etc.) from audio files using extracted voice features.

## 📁 Dataset Used
- **RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song)**

## 🛠 Tools & Libraries
- Python
- Librosa (for audio processing & MFCC feature extraction)
- Pandas (for dataset management)
- Scikit-learn (for training and evaluation)
- Joblib (for saving models)
- Streamlit *(optional)* for UI

## 🧠 Model
- **SVM (Support Vector Machine)** with linear kernel
- Feature: Mean MFCCs from each audio sample

## 🚀 How to Run
1. Install required libraries:
   ```bash
   pip install librosa pandas scikit-learn joblib streamlit
   ```
2. Place RAVDESS audio files in a folder (e.g., `data/`).
Visit the RAVDESS Emotional Speech Audio page on Kaggle.
3. Run the training script to create and save the model.
4. *(Optional)* Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📊 Output
- The model will predict the emotion from `.wav` files and show accuracy metrics.
- The app allows real-time emotion detection from uploaded speech files.

## 📄 Report
A 2-page PDF report is included (`Speech_Emotion_Detection_Report.pdf`) summarizing the project.

---

Created for learning and academic demonstration purposes.
