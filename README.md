<a id="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Multivariate LSTM Stock Price Predictor</h3>

  <p align="center">
    An interactive deep learning web application that forecasts stock price trends using historical market data, technical indicators, and Recurrent Neural Networks (LSTM).
    <br />
    <a href="https://rja-stock-price-prediction-lstm.streamlit.app/"><strong>View Live Web App »</strong></a>
    <br />
    <br />
    <a href="https://rja-stock-price-prediction-lstm.streamlit.app/">Live Demo</a>
    &middot;
    <a href="https://github.com/rabraham360/stock-price-prediction-lstm/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/rabraham360/stock-price-prediction-lstm/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Predicting financial market trends requires analyzing context over time rather than evaluating isolated data points. This project implements a **Multivariate Long Short-Term Memory (LSTM)** deep learning model designed to sequence time-series data and forecast stock trends.

Instead of relying solely on historical closing prices, the neural network processes three synchronized feature inputs:
1. **Closing Price:** Primary target metric.
2. **Trading Volume:** Gauge of market activity and volatility.
3. **20-Day Simple Moving Average (SMA_20):** Calculated trend-momentum indicator.

Data is preprocessed through a 60-day sliding window mechanism, normalized via `MinMaxScaler`, and passed to a stacked LSTM architecture with `Dropout` regularization layers to mitigate overfitting.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.org]][Python-url]
* [![TensorFlow][TensorFlow.org]][TensorFlow-url]
* [![Streamlit][Streamlit.io]][Streamlit-url]
* [![Pandas][Pandas.pydata.org]][Pandas-url]
* [![Plotly][Plotly.com]][Plotly-url]
* [![scikit-learn][scikit-learn.org]][scikit-learn-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Follow these steps to set up and run the project locally on your machine.

### Prerequisites

Ensure you have **Python 3.10 or 3.11** installed (TensorFlow requires Python $\le 3.12$).
* Check Python version:
  ```sh
  python3 --version
  ```

### Installation

1. **Clone the repository:**
   ```sh
   git clone [https://github.com/rabraham360/stock-price-prediction-lstm.git](https://github.com/rabraham360/stock-price-prediction-lstm.git)
   cd stock-price-prediction-lstm
   ```

2. **Install project dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Option 1: Run the Interactive Web Dashboard (Streamlit)
Launch the web interface locally to select custom tickers (e.g., `AAPL`, `MSFT`, `NVDA`, `TSLA`) and customizable date ranges:
```sh
streamlit run app.py
```

### Option 2: Run the Standalone CLI Pipeline
Execute the raw Python pipeline directly from your terminal to generate static `matplotlib` figures saved to your root folder:
```sh
python3 predict.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Baseline Univariate LSTM Model (Closing Price)
- [x] Multivariate Signal Integration (Close + Volume + SMA_20)
- [x] Streamlit Web Dashboard with Interactive Plotly Charts
- [x] Cloud Deployment via Streamlit Community Cloud
- [ ] Display Real-Time Metrics (MAE, RMSE, Loss Curves)
- [ ] Integrate Additional Technical Indicators (RSI, MACD, Bollinger Bands)
- [ ] Multi-Step Future Trend Forecasting (7-day / 30-day forward projections)

See the [open issues](https://github.com/rabraham360/stock-price-prediction-lstm/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions make the open-source community an incredible place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Project Link: [https://github.com/rabraham360/stock-price-prediction-lstm](https://github.com/rabraham360/stock-price-prediction-lstm)

Live Application: [https://rja-stock-price-prediction-lstm.streamlit.app/](https://rja-stock-price-prediction-lstm.streamlit.app/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Yahoo Finance API (`yfinance`)](https://github.com/ranaroussi/yfinance)
* [TensorFlow & Keras Documentation](https://www.tensorflow.org/)
* [Streamlit Cloud Hosting](https://streamlit.io/cloud)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/rabraham360/stock-price-prediction-lstm.svg?style=for-the-badge
[contributors-url]: https://github.com/rabraham360/stock-price-prediction-lstm/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/rabraham360/stock-price-prediction-lstm.svg?style=for-the-badge
[forks-url]: https://github.com/rabraham360/stock-price-prediction-lstm/network/members
[stars-shield]: https://img.shields.io/github/stars/rabraham360/stock-price-prediction-lstm.svg?style=for-the-badge
[stars-url]: https://github.com/rabraham360/stock-price-prediction-lstm/stargazers
[issues-shield]: https://img.shields.io/github/issues/rabraham360/stock-price-prediction-lstm.svg?style=for-the-badge
[issues-url]: https://github.com/rabraham360/stock-price-prediction-lstm/issues
[license-shield]: https://img.shields.io/github/license/rabraham360/stock-price-prediction-lstm.svg?style=for-the-badge
[license-url]: https://github.com/rabraham360/stock-price-prediction-lstm/blob/main/LICENSE
[streamlit-shield]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[streamlit-url]: https://rja-stock-price-prediction-lstm.streamlit.app/

[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[TensorFlow.org]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/
[Streamlit.io]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/
[Pandas.pydata.org]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Plotly.com]: https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white
[Plotly-url]: https://plotly.com/
[scikit-learn.org]: https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white
[scikit-learn-url]: https://scikit-learn.org/
