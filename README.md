# AI Trader Application

This project is an AI trading application that allows for backtesting different trading strategies. You can run the app locally or with Streamlit.

Our Streamlit app: https://quantfin.streamlit.app/

---

## Project Structure
- `app.py`: Main entry file for the Streamlit interface.
- `main.py`: Script for running the main application functionality.
- `backtrader`, `data`, `log`, `pages`, `trading`: Folders containing various modules, data, logs, pages, and trading strategies for the application.

---

## Installation and Requirements
Clone this repository and install the required dependencies:

### For Mac
1. Install **TA-Lib** first:
   ```bash
   brew install ta-lib
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

This project requires Python 3.11 or higher. Non-ARM Macs will need to manually install compatible versions of **Torch** and **TensorFlow**.

---

## Usage

### Running the Application
1. **Run the main Python script**:
   ```bash
   python main.py
   ```

2. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

---

## Note for Streamlit Users
If you want to run the Streamlit app **locally**, you will need to create your own `.streamlit/secrets.toml` file in the root directory to securely store API keys and other secrets. For example:

### Example `.streamlit/secrets.toml`:
```toml
[openai]
api_key = "your-openai-api-key-here"
```

Make sure to replace `"your-openai-api-key-here"` with your actual API key.

---

## Features
- **Pre-built trading strategies**: Includes strategies such as Buy and Hold, Moving Averages, Bollinger Bands, and more.
- **Real-time stock data fetching and visualization**: Allows you to fetch, analyze, and visualize stock data in real-time.
- **Customizable backtesting**: Configure date ranges, stock selections, and other parameters to backtest your strategies.

--- 
