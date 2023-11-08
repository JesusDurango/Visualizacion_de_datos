import pandas as pd
import plotly.graph_objects as go

# Crear un DataFrame con los datos
data = {
    'id': range(1, 21),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

'''fig = go.Figure()

for materia in df['materia'].unique():
    fig.add_trace(go.Box(x=df[df['materia'] == materia]['materia'], y=df[df['materia'] == materia]['nota'], name=materia))

fig.update_layout(title='Boxplot de Notas por Materia')
fig.show()'''


aprobados = df[df['aprobado'] == 'Sí'].shape[0]
no_aprobados = df[df['aprobado'] == 'No'].shape[0]

labels = ['Aprobados', 'No Aprobados']
sizes = [aprobados, no_aprobados]
colors = ['#1f77b4', '#ff7f0e' ]


fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, marker=dict(colors=colors))])

fig.update_layout(title='Distribución de Aprobados', title_x=0.5)
fig.show()

