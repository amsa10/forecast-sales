import tensorflow as tf
import numpy as np

# Generate random sales data for training
np.random.seed(42)
X_train = np.random.uniform(10, 500, 1000)  # Transaction amounts
y_train = X_train * 0.5 + np.random.normal(0, 10, 1000)  # Target (predicted sales)

# Define the model (simple linear regression)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_dim=1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=5)

# Save the model
model.save('./models/sales_model/1/sales_model.h5')
