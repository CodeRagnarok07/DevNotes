import pandas as pd
import matplotlib.pyploy as plt

# open csv data
data = pd.read_csv('car_data.csv', header = none)

data.colums = ['price', 'mant', 'n_doors', 'capacity', 'size_lug', 'safety', 'class'] 

for i in data.colums:
    data.i.sample(3)

    # data[i].replace(tuple(data[i].value_conts()), for i in len(data[i].value_conts() i ))


