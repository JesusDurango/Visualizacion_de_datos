import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear un DataFrame con los datos
data = {
    'id': range(1, 21),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Crea el boxplot
plt.style.use('fivethirtyeight')
plt.figure(figsize=(10, 6))
plt.boxplot([df[df['materia'] == 'Matemáticas']['nota'],
             df[df['materia'] == 'Historia']['nota'],
             df[df['materia'] == 'Ciencias']['nota'],
             df[df['materia'] == 'Lenguaje']['nota']],
            labels=['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'])
plt.title('Distribución de Notas por Materia')
plt.ylabel('Nota')
plt.show()

#Crea grafico de torta

aprobados = df[df['aprobado'] == 'Sí'].shape[0]
no_aprobados = df[df['aprobado'] == 'No'].shape[0]

labels = ['Aprobados', 'No Aprobados']
sizes = [aprobados, no_aprobados]
colors = ['#1f77b4', '#ff7f0e' ]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels,colors = colors,autopct='%1.1f%%',startangle= 90)


plt.title('Distribuición de Aprobados')
plt.show()