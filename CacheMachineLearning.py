from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


class Cache:
    data_features = []
    labels = []

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.data_features = []
        self.labels = []
        self.model = LogisticRegression()
        self._is_fitted = False
        self._counter = len(self.data_features)
        self.misses = 0
        self.hits = 0

    def access_data(self, data):
        if data in self.cache:
            self.data_features.append(data)
            self.labels.append(1) # Se considera un Hit
            self._counter = self._counter + 1
            self.hits = self.hits + 1
            print("Hit!")
        else:
            index_to_insert = None
            if not self._is_fitted and len(self.cache) >= self.capacity and self._counter < 10:
                self.cache.pop(0)
            elif self._is_fitted and self._counter <= 10:
                for element in self.cache:
                    pred = self.model.predict(np.array(element).reshape(1, -1))
                    if pred == 0:
                        index_to_insert = self.cache.index(element)
                        self.cache[index_to_insert]= data
                        self.cache.append(data)
                        self.data_features.append(data)
                        self.labels.append(0) # Se considera un Miss
                        self._counter = self._counter + 1
                        self.misses = self.misses + 1
                        print("Miss!")
                        return
            elif self._counter == 10:
                self.train_model()
                self._counter = 0
                self._is_fitted = True
                for element in self.cache:
                    pred = self.model.predict(np.array(element).reshape(1, -1))
                    if pred == 0:
                        index_to_insert = self.cache.index(element)
                        self.cache[index_to_insert]= data
                        self.data_features.append(data)
                        self.labels.append(0) # Se considera un Miss
                        self._counter = self._counter + 1
                        self.misses = self.misses + 1
                        print("Miss!")
                        return
                self.cache.pop(0)
            self.cache.append(data)
            self.data_features.append(data)
            self.labels.append(0) # Se considera un Miss
            self._counter = len(self.data_features)
            self.misses = self.misses + 1
            print("Miss!")


    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.data_features, self.labels, test_size=0.2)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        self._is_fitted = True
        self._counter = 0
        self.data_features = []
        self.labels = []
        print("Model Accuracy:", accuracy)




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