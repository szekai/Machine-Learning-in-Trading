import pandas as pd
import matplotlib.pyplot as plt

def get_max_close(symbol):
    """
    Return the maximun closing value for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data
    return df['Close'].max() # compute and return max

def get_mean_volumn(symbol):
    """
    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data
    return df['Volume'].mean()  # compute and return mean

def test_run():
    """Function called by Test Run."""
    # for symbol in ['APPL', 'IBM']:
    #     print("Max close")
    #     print(symbol, get_max_close(symbol))
    #
    # for symbol in ['APPL', 'IBM']:
    #     print("Mean Volume")
    #     print(symbol, get_mean_volumn(symbol))

    # df = pd.read_csv("data/APPL.csv")
    # print(df['Adj Close'])
    # df['Adj Close'].plot()
    # plt.show()  # must be called to show plots
    #
    # df2 = pd.read_csv("data/IBM.csv")
    # print(df2['High'])
    # df2['High'].plot()
    # plt.show()  # must be called to show plots


    df = pd.read_csv("data/IBM.csv")
    df[['Close', 'Adj Close']].plot()
    plt.show()


if __name__ == "__main__":
    test_run()
