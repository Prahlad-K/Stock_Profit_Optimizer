import numpy as np
import pandas as pd
from gym.utils import seeding
import gym
from gym import spaces

import matplotlib.pyplot as plt
import pickle

data_1 = pd.read_csv('/home/prahlad/myenv/lib/python3.7/site-packages/gym/envs/zxstock/Data_Daily_Stock_Dow_Jones_30/dow_jones_30_daily_price.csv')
select_stocks_list = ['AAPL']

data_2 = data_1[data_1.tic.isin(select_stocks_list)][~data_1.datadate.isin(['20010912','20010913'])]

data_3 = data_2[['iid','datadate','tic','prccd','ajexdi']]

data_3['adjcp'] = data_3['prccd'] / data_3['ajexdi']

train_data = data_3[(data_3.datadate > 20090000) & (data_3.datadate < 20190000)]

dates = train_data['datadate'].values.tolist()

with open("twitter_dates.txt", "wb") as fp:
	pickle.dump(dates, fp)

with open("twitter_dates.txt", "rb") as fp:
	b = pickle.load(fp)

print(b)
print(len(b))