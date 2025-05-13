# Streamlit Web App
import streamlit as st
import librosa
import numpy as np
import joblib

model = joblib.load('emotion_model.joblib')

st.title('Speech Emotion Detector')
uploaded = st.file_uploader('Upload a WAV file', type=['wav'])

if uploaded:
    signal, sr = librosa.load(uploaded, sr=22050)
    mfcc = np.mean(librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=13).T, axis=0).reshape(1, -1)
    prediction = model.predict(mfcc)[0]
    st.success(f'Detected Emotion: **{prediction}**')
