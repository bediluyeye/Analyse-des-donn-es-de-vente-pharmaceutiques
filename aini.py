import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Chargement et preparation
df = pd.read_csv('data/salesdaily.csv', sep=';')
df['datum'] = pd.to_datetime(df['datum'])
df['year'] = df['datum'].dt.year
df['month'] = df['datum'].dt.month
df['weekday_name'] = df['datum'].dt.day_name()
title = []
for titre in df.columns:
    title.append(titre)
print(title)

