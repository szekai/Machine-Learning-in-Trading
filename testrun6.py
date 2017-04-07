import pandas as pd
import utils
import matplotlib.pyplot as plt


def test_run():
    # Read data
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GOOG', 'GLD']
    df = utils.get_data(symbols, dates)


    # Compute Bollinger Bands
    # 1. Compute rolling mean
    rm_SPY = utils.get_rolling_mean(df['SPY'], window=20)

    # 2. Compute rolling standard deviation
    rstd_SPY = utils.get_rolling_std(df['SPY'], window=20)

    # 3. Compute upper and lower bands
    (upper_band, lower_band) = utils.get_bollinger_bonds(rm_SPY, rstd_SPY)

    # Plot raw SPY value,  rolling mean  and Bollinger Bands
    ax = df['SPY'].plot(title="Bollinger Bands", label='SPY')
    rm_SPY.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and lengend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()



if __name__ == "__main__":
    test_run()