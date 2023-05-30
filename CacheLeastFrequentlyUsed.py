from collections import defaultdict

from collections import defaultdict

class Cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.misses = 0
        self.hits = 0
        self.frequency = defaultdict(int)  # Contador de frecuencia para cada dato en la cache

    def access_data(self, data):
        key = tuple(data)  # Convertir la lista en una tupla
        if key in self.cache:
            print("Hit!")
            self.hits += 1
            self.frequency[key] += 1  # Incrementar la frecuencia del dato
        else:
            if len(self.cache) >= self.capacity:
                # Encontrar el dato menos frecuentemente utilizado
                least_frequent_data = min(self.frequency, key=self.frequency.get)
                self.cache.remove(least_frequent_data)  # Eliminar el dato menos frecuente
                del self.frequency[least_frequent_data]  # Eliminar su contador de frecuencia
            self.cache.append(key)
            self.frequency[key] += 1  # Incrementar la frecuencia del nuevo dato
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