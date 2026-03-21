import os
import tensorflow as tf

MODELPATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'plant_disease_model.h5')


def load_model():
    if not os.path.exists(MODELPATH):
        raise FileNotFoundError(f"Vision model not found: {MODELPATH}")

    model = tf.keras.models.load_model(MODELPATH)
    return model

