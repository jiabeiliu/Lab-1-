import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, ReLU, Sigmoid

# Define the model
model = Sequential()

# Layer 1: 10 neurons, ReLU activation
model.add(Dense(10, input_dim=your_input_dimension, activation='relu'))

# Layers 2 and 3: 8 neurons each, ReLU activation
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))

# Layer 4: 4 neurons, ReLU activation
model.add(Dense(4, activation='relu'))

# Layer 5: 1 neuron, Sigmoid activation (for binary classification)
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Summary of the model
model.summary()
