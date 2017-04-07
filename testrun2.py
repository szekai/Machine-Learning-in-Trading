''' Build a dataframe in pandas'''
import pandas as pd
import utils


def test_run():
    start_date='2010-01-01'
    end_date='2010-12-31'
    dates=pd.date_range(start_date,end_date)

    #Read in more stocks
    symbols = ['GOOG','IBM','GLD']
    df = utils.get_data(symbols,dates)

    # Slice by row range (dates) using DataFrame.ix[] selector
    # print(df.ix['2010-01-01':'2010-01-31'])

    # Slice by column (symbols)
    # print(df[GOOG']  # a single label selects a single column
    # print(df[['IBM','GLD']])  # a list of labels seleccts multiple columns

    # Slice by row and column
    # print(df.ix['2010-03-10':'2010-03-15', ['SPY', 'IBM']])

    utils.plot_data(utils.normalize_data(df))
    # utils.plot_selected(df, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')

if __name__ == "__main__":
    test_run()