import pandas as pd
import numpy as np
import re
import sys
import pyper
from time import sleep



def cleansing(one_day):
    half = int(one_day.shape[0]/2)
    one_day = one_day.iloc[:half]
    one_day = one_day.drop('Unnamed: 0', axis=1)

    for i in range(one_day.shape[0]):
        if one_day.loc[i, 'e_win'] == 1.0:
            one_day.loc[i, 'e_rikishi'], one_day.loc[i, 'w_rikishi'] = one_day.loc[i, 'w_rikishi'], one_day.loc[i, 'e_rikishi']
        elif one_day.loc[i, 'e_win'] == 0.0:
            pass
        elif one_day.loc[i, 'e_win'] == 1.01 or one_day.loc[i, 'e_win'] == -0.1:
            one_day = one_day.drop(i, axis=0)
        else:
            sys.exit(f'cleansing error: {year}, {month}, {day}')

    one_day = one_day.drop(['e_win', 'w_win'], axis=1)
    one_day.columns = ['loser', 'winner']
    one_day['year'] = year
    one_day['month'] = month
    one_day['day'] = day
    return one_day




if __name__ == '__main__':
    year_list = [
        '2001', '2002', '2003', '2004', '2005',
        '2006', '2007', '2008', '2009', '2010', '2011',
        '2012', '2013', '2014',
        '2015', '2016', '2017', '2018'
    ]
    month_list = ['01', '03', '05', '07', '09', '11']
    day_list = range(1, 16)
    data = pd.DataFrame(columns=['loser', 'winner', 'year', 'month', 'day'])

    for year in year_list:
        for month in month_list:
            for day in day_list:
                fname = year+month+f'&day={day}_bt.csv'
                try:
                    one_day = pd.read_csv(f'input/{fname}')
                except:
                    print(f'"{fname}" is not here')
                else:
                    one_day = cleansing(one_day)
                    data = pd.concat([data, one_day], axis=0)
    data = data.reset_index(drop=True)
    data.to_csv('data.csv')
    # sys.exit()


#200205, 201103, 201105はデータが丸々ない
