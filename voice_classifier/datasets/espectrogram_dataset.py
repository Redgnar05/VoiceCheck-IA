
# /voice_classifier/datasets/espectrogram_dataset.py

import os
import torch
from torch.utils.data import Dataset
from utils.audio_processing import cargar_y_normalizar_espectrograma

class EspectrogramaDataset(Dataset):
    def __init__(self, carpeta, etiquetas):
        self.carpeta = carpeta
        self.archivos = [f for f in os.listdir(carpeta) if f.endswith('.wav')]
        self.etiquetas = etiquetas

    def __len__(self):
        return len(self.archivos)

    def __getitem__(self, idx):
        archivo = self.archivos[idx]
        etiqueta = torch.tensor([self.etiquetas[archivo]], dtype=torch.float32)
        ruta = os.path.join(self.carpeta, archivo)
        tensor = cargar_y_normalizar_espectrograma(ruta)
        return tensor, etiqueta






