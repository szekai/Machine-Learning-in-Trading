"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
                              usecols=['Date', 'Adj Close'], na_values=['nan'])

        # rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  #drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df

def plot_data(df, title="Stock prices",xlabel="Date", ylabel="Price"):
    '''Plot stock prices'''
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show() # must be called to show plots in some environments


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired column over index values in the given range."""
    plot_data(df.ix[start_index:end_index, columns], title="Selected data")

def normalize_data(df):
    """Normalize stock prices using the first row of the dataframes"""
    return df/df.ix[0,:]

def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""
    return pd.rolling_mean(values, window=window)

def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    return pd.rolling_std(values, window=window)

def get_bollinger_bonds(rm, rstd):
    """Return upper and lower Bollinger Bands"""
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    return upper_band, lower_band

def compute_daily_returns(df):
    """Compute and return daily return values"""
    daily_returns = df.copy() # copy given DataFrame to match size and column names
    # compute daily returns for row 1 onwards
    # daily_returns[1:] = (df[1:]/df[:-1].values) - 1
    daily_returns[1:] = (df/df.shift(1)) -1
    daily_returns.ix[0,:] = 0  # Pandas leaves the 0th row full of Nans
    return daily_returns

def compute_cumulative_returns(df):
    cumulative_returns = (df/df.ix[0,:]) -1
    return cumulative_returns