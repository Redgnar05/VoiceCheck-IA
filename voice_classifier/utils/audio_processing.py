

# /voice_classifier/utils/audio_processing.py


import librosa
import numpy as np
import torch

def cargar_y_normalizar_espectrograma(ruta, longitud_fija=300):
    y, sr = librosa.load(ruta, sr=22050)
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=512, n_mels=128)
    S_db = librosa.amplitude_to_db(S, ref=np.max)
    S_db_norm = (S_db - S_db.min()) / (S_db.max() - S_db.min())

    # Ajustar la longitud temporal
    if S_db_norm.shape[1] < longitud_fija:
        # Rellenar con ceros si es más corto
        pad_width = longitud_fija - S_db_norm.shape[1]
        S_db_norm = np.pad(S_db_norm, ((0, 0), (0, pad_width)), mode='constant')
    else:
        # Recortar si es más largo
        S_db_norm = S_db_norm[:, :longitud_fija]

    tensor = torch.tensor(S_db_norm, dtype=torch.float32).unsqueeze(0)  # (1, 128, longitud_fija)
    return tensor






