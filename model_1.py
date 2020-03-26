import pandas_datareader as pdr
import datatime
import numpy as np

vale3 = pdr.get_data_yahoo('VALE3.SA', start=datatime.datatime(2016,10,1), end=datatime.datatime(2019,1,1))

display(vale3.head())