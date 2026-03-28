
import tensorflow as tf
from tensorflow.keras import layers, models

def createModel(input_shape=(100, 100, 1)):
    model = models.Sequential([
        # --- Bloque 1: Detección de bordes básicos ---
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),

        # --- Bloque 2: Patrones más complejos (esquinas, formas) ---
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),

        # --- Bloque 3: Refinamiento de características ---
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),

        # --- Bloque 4: Capas profundas de decisión ---
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),  # Evita que la red se "sobreajuste"
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.2),

        # --- Output: Regresión lineal para conteo ---
        layers.Dense(1, activation='linear')
    ])

    # Usamos un optimizador con un aprendizaje controlado
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='mse',
        metrics=['mae']
    )

    return model
