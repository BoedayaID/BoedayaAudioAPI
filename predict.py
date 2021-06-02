import librosa
import numpy as np
import soundfile as sf
import tensorflow as tf

SAVED_MODEL_PATH = "model.h5"
AUDIO_LENGTH = 64000

model = None
mapping = [
    "atas",
    "bawah",
    "kamu",
    "kanan",
    "kiri",
    "maju",
    "makan",
    "minum",
    "mundur",
    "saya"
]

def preprocess(file_path, num_mfcc=13, n_fft=2048, hop_length=512):
        signal, sample_rate = librosa.load(file_path)     
        if len(signal) >= AUDIO_LENGTH:
            signal = signal[:AUDIO_LENGTH]
            MFCCs = librosa.feature.mfcc(signal, sample_rate, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
        else:
            signal1 = np.zeros((AUDIO_LENGTH,))
            signal1[:signal.shape[0]] = signal
            sf.write(file_path, signal1, sample_rate)
            MFCCs = librosa.feature.mfcc(signal, sample_rate, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
        return MFCCs.T


def prediction(file_path):
        model = tf.keras.models.load_model("model.h5")
        MFCCs = preprocess(file_path)
        MFCCs = MFCCs[np.newaxis, ..., np.newaxis]
        predictions = model.predict(MFCCs)
        predicted_index = np.argmax(predictions)
        predicted_keyword = mapping[predicted_index]
        return predicted_keyword