

# /voice_classifier/predict.py


import torch
from models.cnn_lstm import MiModelo
from utils.audio_processing import cargar_y_normalizar_espectrograma

if __name__ == "__main__":
    modelo = MiModelo()
    modelo.load_state_dict(torch.load("modelo_entrenado.pth"))  # Carga los pesos
    modelo.eval()

    ruta_test = "data/Filosofia.wav"
    tensor = cargar_y_normalizar_espectrograma(ruta_test).unsqueeze(0)

    with torch.no_grad():
        salida = modelo(tensor)
        print(f"Probabilidad de que sea voz real: {salida.item():.4f}")















