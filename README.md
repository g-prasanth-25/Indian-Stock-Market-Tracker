# Indian Stock Market Tracker

## Overview
This script fetches and analyzes stock market data from Yahoo Finance for Indian companies listed on NSE (National Stock Exchange) and BSE (Bombay Stock Exchange). It provides functionalities to calculate moving averages and visualize stock price trends along with trading volumes.

## Features
- Fetch historical stock data for NSE and BSE companies.
- Calculate and plot moving averages (20-day and 50-day by default).
- Visualize stock closing prices and trading volumes.

## Requirements
- Python 3.7 or higher
- Required Python packages:
  - `yfinance`
  - `matplotlib`

You can install the required packages using:
```bash
pip install yfinance matplotlib
```

## How to Use

1. Clone or download the repository.
2. Run the script:
```bash
python script_name.py
```
3. Follow the prompts:
   - Choose the stock exchange (`NSE` or `BSE`).
   - Enter the company name or symbol (e.g., `RELIANCE`, `TCS`).
   - Enter the start and end dates for the data range (in `YYYY-MM-DD` format).

4. The script will fetch the stock data, calculate moving averages, and display a plot with the stock price and optional volume data.

## Example
1. **Input:**
   ```
   Choose Exchange (NSE/BSE): NSE
   Enter Company Name or Symbol (e.g., RELIANCE, TCS): RELIANCE
   Enter Start Date (YYYY-MM-DD): 2023-01-01
   Enter End Date (YYYY-MM-DD): 2023-12-31
   ```
2. **Output:**
   - A plot showing RELIANCE's closing prices and moving averages for the selected date range.

## Functions

### `fetch_stock_data(ticker, start_date, end_date)`
Fetch historical stock data for a given ticker and date range.
- **Parameters:**
  - `ticker`: Ticker symbol (e.g., `RELIANCE.NS` for NSE).
  - `start_date`: Start date (YYYY-MM-DD).
  - `end_date`: End date (YYYY-MM-DD).
- **Returns:** Pandas DataFrame with stock data.

### `calculate_moving_average(data, window_size)`
Calculate the moving average for the given window size.
- **Parameters:**
  - `data`: Stock data DataFrame.
  - `window_size`: Number of days for the moving average.
- **Returns:** Series with the calculated moving average.

### `plot_stock_data(data, ticker, moving_averages=None, show_volume=False)`
Plot stock data with optional moving averages and trading volume.
- **Parameters:**
  - `data`: Stock data DataFrame.
  - `ticker`: Company ticker name.
  - `moving_averages`: Dictionary of moving averages to plot.
  - `show_volume`: Boolean to show trading volume on the plot.

## Notes
- Ensure the company symbol and exchange combination is valid.
- The script handles missing or invalid data gracefully.

## License
This project is licensed under the MIT License.

---