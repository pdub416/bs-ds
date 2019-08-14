import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import bokeh as bk

df_planes = pd.read_csv('planes.csv')
df_flights = pd.read_csv('flights.csv')

#planes = ['tailnum', 'year', 'type', 'manufacturer', 'model', 'engines', 'seats', 'speed', 'engine']
#flights = [['year', 'month', 'day', 'dep_time', 'sched_dep_time', 'dep_delay','arr_time', 'sched_arr_time', 'arr_delay', 'carrier', 'flight','tailnum', 'origin', 'dest', 'air_time', 'distance', 'hour', 'minute','time_hour']

planes2 = df_planes[['tailnum','model']]

# model with most flights out of NY in 2013
df = pd.merge(df_flights,planes2,on='tailnum',how='left')
df.head()

df2 = df[(df['year'] == 2013) & df['origin'].isin(['LGA','JFK','EWR'])]
df2g = df2.groupby('model').agg(len)

pass