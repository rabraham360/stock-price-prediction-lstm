import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

df = yf.download("AAPL", start="2019-01-01",end="2024-01-01")

df['SMA_20'] = df['Close'].rolling(window=20).mean()
df = df.dropna()

feature_cols = ['Close', 'Volume', 'SMA_20']
feature_data = df[feature_cols].values
target_data = df[['Close']].values

feature_scaler = MinMaxScaler(feature_range=(0,1))
target_scaler = MinMaxScaler(feature_range=(0,1))

scaled_features = feature_scaler.fit_transform(feature_data)
scaled_target = target_scaler.fit_transform(target_data)

x_data, y_data = [], []
for i in range(60, len(scaled_features)):
    x_data.append(scaled_features[i-60:i])
    y_data.append(scaled_target[i, 0])

x_data, y_data = np.array(x_data), np.array(y_data)

split = int(len(x_data) * 0.8)
x_train, x_test = x_data[:split], x_data[split:]
y_train, y_test = y_data[:split], y_data[split:]

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], x_train.shape[2])),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, batch_size=32, epochs=20, validation_data=(x_test, y_test))

predictions = model.predict(x_test)
predictions = target_scaler.inverse_transform(predictions)
actual = target_scaler.inverse_transform(y_test.reshape(-1, 1))

plt.figure(figsize=(12, 6))
plt.plot(actual, label='Actual Price', color='blue')
plt.plot(predictions, label='Predicted Price (Multivariate)', color='red')
plt.title('AAPL Stock Price Prediction (Close + Volume + SMA_20)')
plt.xlabel('Days')
plt.ylabel('Price ($)')
plt.legend()
plt.show()