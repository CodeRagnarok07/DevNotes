
import pandas as pd
import matplotlib.pyplot as plt
# open file

data = pd.read_csv('../car.csv', header=None)

data.columns = ['Price', 'Maintenance Cost', 'Number of Door','Capacity', 'Size of', 'Safety' , 'Decision']

#data_w_color = data['Price'].replace(('valor definido','','',''), (1,2,3,"nuevo nombre campo")) # cambia el campo de los valores unicos

prices = data['Price'].value_counts()

# grafica como barra
colors = ['#24246e','#45468e','#78946e','#24246e' ]
prices.plot(kind='bar', color=colors) 
# definicion de parametros

plt.xlabel('precio')
plt.ylabel('autos')
plt.title("precios de autos")

plt.show()
plt.savefig("./grf.png")
