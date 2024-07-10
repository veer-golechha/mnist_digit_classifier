import keras
import numpy as np

# model path to the model binary
model_path = "./mnist_97acc.h5"


class mnist_model:
    def __init__(self) -> None:
        """Model Object used to simplify `mnist model` integration."""

        self.model = keras.models.load_model(model_path)
        self.prediction = None

    def predict(self, arr: np.ndarray) -> None:
        """Saves the `model` prediction in `prediction`.

        Parameters
        ----------
        arr : np.ndarray
            accepts numpy array (required shape: 1x784)
        """

        self.prediction = self.model.predict(arr)

    def reset(self) -> None:
        """Clears the `prediction`."""

        self.prediction = None
