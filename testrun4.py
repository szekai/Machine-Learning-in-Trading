import pandas as pd
import utils

def test_run():
    # Read data
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GOOG', 'GLD']
    df = utils.get_data(symbols, dates)
    utils.plot_data(df)

    #Compute global statistic for each stock
    print(df.mean())

if __name__ == "__main__":
    test_run()