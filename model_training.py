import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import tensorflow_datasets as tfds

#method for loading the emnist data
def load_emn():
    try:
        ds_train, ds_test = tfds.load('emnist/letters', split=['train', 'test'], as_supervised=True, shuffle_files=False)
        #dataset to numpy arrays conversion
        ds_train_batched = ds_train.batch(1000)
        ds_test_batched = ds_test.batch(1000)
        x_train_batches, y_train_batches = [], []
        for batch in ds_train_batched:
            x_train_batches.append(batch[0].numpy())
            y_train_batches.append(batch[1].numpy())
        x_test_batches, y_test_batches = [], []
        for batch in ds_test_batched:
            x_test_batches.append(batch[0].numpy())
            y_test_batches.append(batch[1].numpy())
        x_train = np.concatenate(x_train_batches, axis=0)
        y_train = np.concatenate(y_train_batches, axis=0)
        x_test = np.concatenate(x_test_batches, axis=0)
        y_test = np.concatenate(y_test_batches, axis=0)
        #Great Success!
        print("Dataset loaded successfully!")
        return (x_train, y_train), (x_test, y_test)
    except Exception as e:
        #hopefully we don't see this
        print(f"Error loading dataset: {e}")

#data loading and preparation
(x_train, y_train), (x_test, y_test) = load_emn()
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = x_train.reshape((-1, 28, 28, 1))
x_test = x_test.reshape((-1, 28, 28, 1))

#CNN BUILDING!!!!
model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(27, activation="softmax")
])

#model compilation and training
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(x_train, y_train, epochs=5)

#saving of initial model
model.save("simple_model.h5")
print("Model has been saved")
