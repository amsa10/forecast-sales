import tensorflow as tf
import numpy as np


# Define the model 

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=5)

# Save the model
model.save('./models/sales_model/1/sales_model.h5')
