import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import bokeh as bk

df_planes = pd.read_csv('planes.csv')
df_flights = pd.read_csv('flights.csv')

df_planes.columns()
df_flights.head()