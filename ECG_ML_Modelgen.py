import math
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from tinymlgen import port
from pandas import read_csv


def get_model():
    ECG_data = read_csv('ECG_features.csv', header=0, index_col=0)
    SAMPLES = 5000
    np.random.seed(1337)
    x_values = np.arange(0, 4999, 1)
    # shuffle and add noise
    print(ECG_data)
    y_values = ECG_data['sensor'].tolist()
    print(y_values)
    print(x_values)

    # split into train, validation, test
    TRAIN_SPLIT =  int(0.6 * SAMPLES)
    TEST_SPLIT = int(0.2 * SAMPLES + TRAIN_SPLIT)
    x_train, x_test, x_validate = np.split(x_values, [TRAIN_SPLIT, TEST_SPLIT])
    y_train, y_test, y_validate = np.split(y_values, [TRAIN_SPLIT, TEST_SPLIT])

    # create a NN with 2 layers of 16 neurons
    model = tf.keras.Sequential()
    model.add(layers.Dense(8, activation='relu', input_shape=(1,)))
    model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    model.fit(x_train, y_train, epochs=500, batch_size=16,
                        validation_data=(x_validate, y_validate))
    return model


def test_model(model, verbose=False):
    x_test = np.random.uniform(low=0, high=2*math.pi, size=100)
    y_test = np.sin(x_test)
    y_pred = model.predict(x_test)
    print('MAE', np.abs(y_pred - y_test).mean())

model = get_model()
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_model = converter.convert()
test_model(model)

# Save the model to disk
open("ECG_ML_model_quantized.tflite", "wb").write(tflite_model)

# Port to C
c_code = port(model, pretty_print = True, optimize=False)
c_file = open("ECG_ML_Model.h", "w")
c_file.write(c_code)
