import pandas as pd
import utils
import matplotlib.pyplot as plt

def test_run():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM']
    df = utils.get_data(symbols, dates)

    # Compute daily returns
    daily_returns = utils.compute_daily_returns(df)

    # #Plot histogram directly from dataframe
    # daily_returns.hist(bins=20)
    # plt.show()

    # Compute and plot both histograms on the same chart
    daily_returns['SPY'].hist(bins=20, label="SPY")
    daily_returns['XOM'].hist(bins=20, label="XOM")
    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    test_run()