import yfinance as yf
import matplotlib.pyplot as plt

#fetch data
def fetch_stock_data(ticker, start_date, end_date):
    """Fetch historical stock data from Yahoo Finance."""
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        if stock_data.empty:
            raise ValueError("No data found for the specified ticker and date range.")
        return stock_data
    except Exception as e:
        print(f"Error fetching stock data for {ticker}: {e}")
        return None


def calculate_moving_average(data, window_size):
    """Calculate the moving average for a given window size."""
    return data['Close'].rolling(window=window_size).mean()


def plot_stock_data(data, ticker="Stock", moving_averages=None, show_volume=False):
    """Plot stock data with optional moving averages and volume."""
    plt.figure(figsize=(12, 8))

    # Plot Close Price
    plt.plot(data['Close'], label=f"{ticker} Close Price (INR)", color='blue')

    # Plot Moving Averages
    if moving_averages:
        for days, ma in moving_averages.items():
            plt.plot(ma, label=f"{days}-Day MA (INR)", linestyle='--')

    plt.title(f"{ticker} Stock Price Analysis (INR)")
    plt.xlabel("Date")
    plt.ylabel("Price (INR)")
    plt.legend()
    plt.grid()

    # Plot Volume on Secondary Axis

    plt.show()


if __name__ == "__main__":
    print("Indian Stock Market Tracker (Prices in INR)")

    # Select exchange
    exchange = input("Choose Exchange (NSE/BSE): ").upper()

    # Input company name or symbol
    company_name = input("Enter Company Name or Symbol (e.g., RELIANCE, TCS): ").upper()

    # Determine the full ticker
    if exchange == "NSE":
        ticker_symbol = f"{company_name}.NS"
    elif exchange == "BSE":
        ticker_symbol = f"{company_name}.BO"
    else:
        print("Invalid exchange selected.")
        exit()

    # Input date range
    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")

    # Fetch data and perform operations
    stock_data = fetch_stock_data(ticker_symbol, start_date, end_date)

    if stock_data is not None:
        # Calculate moving averages
        ma_20 = calculate_moving_average(stock_data, 20)
        ma_50 = calculate_moving_average(stock_data, 50)

        moving_averages = {"20": ma_20, "50": ma_50}

        # Automatically show the plot
        plot_stock_data(stock_data, company_name, moving_averages)
    else:
        print("No data found. Please check the ticker or date range.")
