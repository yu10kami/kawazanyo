#coding:utf-8
import pandas as pd
from typing import Tuple
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

def income(ticker:str, purchase_info:list) -> Tuple[str, list, float]:
    df = pdr.get_data_yahoo('{}.T'.format(ticker), progress=False)
    diff = []
    for i in range(len(purchase_info)):
        diff.append(float('{:.2f}'.format((df['Close'][-1]-purchase_info[i][1])*purchase_info[i][0])))
    return df.index[-1].strftime('%Y%m%d'), diff, sum(diff)

def kawazanyo(purchase_info:list, future_price:float) -> Tuple[list, float]:
    diff = []
    for i in range(len(purchase_info)):
        diff.append(float('{:.2f}'.format((future_price-purchase_info[i][1])*purchase_info[i][0])))
    return diff, sum(diff)