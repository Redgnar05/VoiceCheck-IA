

# voice_chain/blockchain.py

import time
import hashlib
import json

class Bloque:
    def __init__(self, index, datos, anterior_hash):
        self.index = index
        self.timestamp = time.time()
        self.datos = datos  # Diccionario con info del audio
        self.anterior_hash = anterior_hash
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        bloque_str = f"{self.index}{self.timestamp}{self.datos}{self.anterior_hash}"
        return hashlib.sha256(bloque_str.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.cadena = [self.crear_bloque_genesis()]

    def crear_bloque_genesis(self):
        return Bloque(0, {"mensaje": "Bloque Génesis"}, "0")

    def agregar_bloque(self, datos):
        ultimo_bloque = self.cadena[-1]
        nuevo_bloque = Bloque(len(self.cadena), datos, ultimo_bloque.hash)
        self.cadena.append(nuevo_bloque)

    def mostrar(self):
        for bloque in self.cadena:
            print(json.dumps({
                "index": bloque.index,
                "timestamp": bloque.timestamp,
                "datos": bloque.datos,
                "anterior_hash": bloque.anterior_hash,
                "hash": bloque.hash
            }, indent=4))









