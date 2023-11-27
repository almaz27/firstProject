# Import the necessary modules and libraries
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from numpy import set_printoptions

from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from deputy_votings import deputy_votes
from sklearn.model_selection import train_test_split

df_dalabayevich = deputy_votes('Токторбаев Ж.Ш.')
print(df_dalabayevich.columns)
print(df_dalabayevich.iloc[45,2])
print(df_dalabayevich.iloc[45,2].rfind(','))

df_dalabayevich['initiators_only'] = df_dalabayevich['initiators'].map(lambda initiator: initiator.replace(initiator[initiator.rfind(','):-1],''))


# print(df_dalabayevich['initiators_only'][0].replace(',',''))
df_dalabayevich['vote'].value_counts(normalize = True).plot.bar()
