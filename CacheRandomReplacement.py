import random

class Cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.misses = 0
        self.hits = 0

    def access_data(self, data):
        if data in self.cache:
            print("Hit!")
            self.hits += 1
        else:
            if len(self.cache) >= self.capacity:
                # Seleccionar aleatoriamente un índice de la cache
                index = random.randint(0, len(self.cache) - 1)
                self.cache.pop(index)
            self.cache.append(data)
            self.misses += 1
            print("Miss!")






# Ejemplo de uso
cache = Cache(3)  # Capacidad de la memoria caché: 3 elementos

# Características de los datos
data_features = {
    "Dato1": [1, 0, 0],  # Características del Dato1
    "Dato2": [0, 1, 0],  # Características del Dato2
    "Dato3": [0, 0, 1],  # Características del Dato3
    "Dato4": [1, 1, 0],  # Características del Dato4
    "Dato5": [0, 1, 1]   # Características del Dato5
}

# Accesos a la memoria caché
cache.access_data(data_features["Dato1"])  # Miss
cache.access_data(data_features["Dato2"])  # Miss
cache.access_data(data_features["Dato3"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato4"])  # Miss
cache.access_data(data_features["Dato4"])  # Hit
cache.access_data(data_features["Dato5"])  # Miss
cache.access_data(data_features["Dato1"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato4"])  # Hit
cache.access_data(data_features["Dato5"])  # Hit
cache.access_data(data_features["Dato1"])  # Miss
cache.access_data(data_features["Dato2"])  # Miss
cache.access_data(data_features["Dato3"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato4"])  # Miss
cache.access_data(data_features["Dato4"])  # Hit
cache.access_data(data_features["Dato5"])  # Miss
cache.access_data(data_features["Dato1"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato4"])  # Hit
cache.access_data(data_features["Dato5"])  # Hit
cache.access_data(data_features["Dato1"])  # Miss
cache.access_data(data_features["Dato2"])  # Miss
cache.access_data(data_features["Dato3"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato4"])  # Miss
cache.access_data(data_features["Dato4"])  # Hit
cache.access_data(data_features["Dato5"])  # Miss
cache.access_data(data_features["Dato1"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato4"])  # Hit
cache.access_data(data_features["Dato5"])  # Hit
cache.access_data(data_features["Dato1"])  # Miss
cache.access_data(data_features["Dato2"])  # Miss
cache.access_data(data_features["Dato3"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato4"])  # Miss
cache.access_data(data_features["Dato4"])  # Hit
cache.access_data(data_features["Dato5"])  # Miss
cache.access_data(data_features["Dato1"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato2"])  # Miss
cache.access_data(data_features["Dato2"])  # Hit
cache.access_data(data_features["Dato4"])  # Hit
cache.access_data(data_features["Dato5"])  # Hit
print("Misses",cache.misses)
print("Hits",cache.hits)