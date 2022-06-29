import pandas as pd
import matplotlib.pyplot as plt
# open file

data = pd.read_csv('car.csv', header=None)

data.columns = ['Price', 'Maintenance Cost', 'Number of Door','Capacity', 'Size of', 'Safety' , 'Decision', 'other']

data.head(5) # mira los primeros 5 datos

data.sample(5) # 5 datos aleatorios

data.tail(2) # ultimos 2

data.shape # muestra la cantidad de columnas y filas

data.size # resultado de datos totales columnas x filas

data['Price'].head() # solo mostrando un campo

data['Capacity'][:3] # rango de atributos tipo lista

data[['Price', 'Maintenance Cost', 'Number of Door','Capacity']].sample() # mas de un campo

# ORDEN DE VALORES

data['Price'].unique() # mustra los valores sin repetir

data['Price'].value_counts() # clasifica por valores iguales ordenado por numero de datos

data['Price'].value_counts().sort_index(ascending= True) # clasifica por valores iguales ordenado por numero de datos

data['Price'].replace(('valor definido','','',''), (1,2,3,"nuevo nombre campo")) # cambia el campo de los valores unicos



# # GRAFICAR
prices = data['Price'].value_counts() # muestra valores agrupados por igual

# grafica como barra
prices.plot(kind='bar') 


colors = ['#DW6566','#DW6566','#DW6566','#DW6566' ]
data_w_color = data['Price'].replace(('valor definido','','',''), (1,2,3,"nuevo nombre campo")) # cambia el campo de los valores unicos
data_w_color.plot(kind='bar', color=colors) 
# definicion de parametros



