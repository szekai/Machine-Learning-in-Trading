import pandas as pd
import utils
import matplotlib.pyplot as plt

def test_run():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY']
    df = utils.get_data(symbols, dates)
    utils.plot_data(df)

    # Compute daily returns
    daily_returns= utils.compute_daily_returns(df)
    utils.plot_data(daily_returns, title="Daily Returns", ylabel="Daily Returns")

    # Plot a histogram
    daily_returns.hist(bins=20)

    # Get mean and standard deviation
    mean = daily_returns['SPY'].mean()
    print("mean=", mean)
    std = daily_returns['SPY'].std()

    plt.axvline(mean,color="w", linestyle="dashed", linewidth=2)
    plt.axvline(std, color="r", linestyle="dashed", linewidth=2)
    plt.axvline(-std, color="r", linestyle="dashed", linewidth=2)
    plt.show()

    # Compute kurtosis
    print(daily_returns.kurtosis()s)
if __name__ == "__main__":
    test_run()