import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

st.set_page_config(page_title="Stock Price Predictor", layout="wide")

st.title("AI Stock Price Prediction App")
st.write("This application uses a Multivariate LSTM (Long Short-Term Memory) neural network to predict stock price trends based on historical market data, volume, and moving averages.")


st.sidebar.header("Configuration")
ticker = st.sidebar.text_input("Stock Ticker", "AAPL").upper()
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2019-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2024-01-01"))

if st.sidebar.button("Run Prediction"):
    with st.spinner(f"Fetching data and training model for {ticker}..."):

        df = yf.download(ticker, start=start_date, end=end_date)
        
        if df.empty:
            st.error("No data found for this ticker. Please check the symbol.")
        else:

            df['SMA_20'] = df['Close'].rolling(window=20).mean()
            df = df.dropna()

            feature_cols = ['Close', 'Volume', 'SMA_20']
            feature_data = df[feature_cols].values
            target_data = df[['Close']].values


            feature_scaler = MinMaxScaler(feature_range=(0, 1))
            target_scaler = MinMaxScaler(feature_range=(0, 1))

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
            model.fit(x_train, y_train, batch_size=32, epochs=10, verbose=0)


            predictions = model.predict(x_test)
            predictions = target_scaler.inverse_transform(predictions)
            actual = target_scaler.inverse_transform(y_test.reshape(-1, 1))


            fig = go.Figure()
            fig.add_trace(go.Scatter(y=actual.flatten(), mode='lines', name='Actual Price', line=dict(color='blue')))
            fig.add_trace(go.Scatter(y=predictions.flatten(), mode='lines', name='Predicted Price', line=dict(color='red')))
            fig.update_layout(
                title=f"{ticker} Stock Price Prediction",
                xaxis_title="Days",
                yaxis_title="Price ($)",
                template="plotly_white"
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.success("Model evaluation complete!")