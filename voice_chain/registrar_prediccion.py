



# voice_chain/registrar_prediccion.py

import os
import hashlib
from blockchain import Blockchain

def hash_archivo(ruta):
    with open(ruta, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    # Simulación de datos de una predicción real
    ruta_audio = "../voice_classifier/data/saludo2.0.wav"
    resultado_prediccion = 0.93  # Simula que salió del modelo

    datos = {
        "archivo": os.path.basename(ruta_audio),
        "hash_audio": hash_archivo(ruta_audio),
        "resultado": resultado_prediccion
    }

    # Crear blockchain e insertar predicción
    cadena = Blockchain()
    cadena.agregar_bloque(datos)
    cadena.mostrar()









