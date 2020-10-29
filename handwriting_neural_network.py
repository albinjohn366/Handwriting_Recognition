import tensorflow as tf
import sys

# Using mnist data-set
data = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = data.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
y_test = tf.keras.utils.to_categorical(y_test)
y_train = tf.keras.utils.to_categorical(y_train)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)

# Creating the model
model = tf.keras.Sequential([

    # convolution layers for 32 filters
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28,
                                                                       28, 1)),

    # Max pool layer
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    # Flattening
    tf.keras.layers.Flatten(),

    # Hidden layer
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),

    # Output layer
    tf.keras.layers.Dense(10, activation='softmax')
])

# Train the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=[
    'accuracy'])
model.fit(x_train, y_train, epochs=20)

# Test the model
model.evaluate(x_test, y_test, verbose=2)

# Save model to file
if len(sys.argv) == 2:
    filename = sys.argv[1]
    model.save(filename)
    print(f"Model saved to {filename}.")
