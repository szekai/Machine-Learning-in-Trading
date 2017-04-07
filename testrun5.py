import pandas as pd
import utils
import matplotlib.pyplot as plt

def test_run():
    # Read data
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY']
    df = utils.get_data(symbols, dates)

    # Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title = "SPY rolling mean", label = 'SPY')

    # Compute rolling mean using a 20-day window
    rm_SPY = pd.rolling_mean(df['SPY'], window=20)

    # Add rolling mean to the same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)

    # Add axis labels and lengend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    test_run()