

# /voice_classifier/train.py


from torch.utils.data import DataLoader
from datasets.espectrogram_dataset import EspectrogramaDataset
from models.cnn_lstm import MiModelo
import torch.nn as nn
import torch.optim as optim
import torch

etiquetas = {
    "Faisy.wav": 0, "Parista.wav": 0,
    "Podcast.wav": 0, "Historia_1.wav": 0,
    "Saludo2.0.wav": 1, "PruebaIA.wav": 0,
    "Filosofia.wav": 1, "Hackaton.wav": 1,
    "Lectura.wav": 1, "Presentacion.wav": 1,
    "Sistema.wav": 1
}

if __name__ == "__main__":
    dataset = EspectrogramaDataset("data", etiquetas)
    dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

    modelo = MiModelo()
    criterio = nn.BCELoss()
    optimizador = optim.Adam(modelo.parameters(), lr=0.001)

    for epoch in range(10):
        modelo.train()
        for entrada, etiqueta in dataloader:
            salida = modelo(entrada)
            perdida = criterio(salida, etiqueta)
            optimizador.zero_grad()
            perdida.backward()
            optimizador.step()
        print(f"Época {epoch+1}: Pérdida = {perdida.item():.4f}")

    torch.save(modelo.state_dict(), "modelo_entrenado.pth")
    print("Modelo guardado en modelo_entrenado.pth")
     








