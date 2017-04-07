import pandas as pd
import utils

def test_run():
    # Read data
    dates = pd.date_range('2012-07-01', '2012-07-31')
    symbols = ['SPY', 'XOM']
    df = utils.get_data(symbols, dates)
    # utils.plot_data(df)

    # Compute daily return
    # daily_returns = utils.compute_daily_returns(df)
    # utils.plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")
    # print(df)
    # print(df[:-1].values)

    cumulative_returns = utils.compute_cumulative_returns(df)
    utils.plot_data(cumulative_returns, title="Cumulative returns", ylabel="Cumulative returns")

if __name__ == "__main__":
    test_run()