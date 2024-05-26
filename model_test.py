from keras.models import Sequential
from keras.layers import Dense

# Example model
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dense(1, activation='sigmoid'))

# Compile and save the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.save('sahil-edited\Stock_Predictions_Model_GOOG.keras')
