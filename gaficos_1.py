import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

"""plt.scatter(matematicas, ciencias, color='blue')
plt.title('Relación entre calificaciones de Matematicas y Ciencias')
plt.xlabel('Calificacion Matematicas')
plt.ylabel('Calificaciones Ciencias')

plt.show()"""



#notas promedio
promedio_matematicas = round(np.mean(matematicas),1)
promedio_ciencias =round(np.mean(ciencias),1)
promedio_literatura = round(np.mean(literatura),1)

#errores promedio
errores_promedio_matematicas =round(np.mean(errores_matematicas),1)
errores_promedio_ciencias =round(np.mean(errores_ciencias),1)
errores_promedio_literatura = round(np.mean(errores_literatura),1)


materias =['Matematicas','Ciencias','Literatura']
promedios = [promedio_matematicas,promedio_ciencias,promedio_literatura]
errores_materias= [errores_promedio_matematicas,errores_promedio_ciencias,errores_promedio_literatura]

"""plt.errorbar(materias,promedios, yerr=errores_materias,fmt = 'o',  capsize=5, label = 'promedio')
plt.xlabel('Materias')
plt.ylabel('Calificaciones Promedio')
plt.title('Calificaciones Promedio con barras de error')
plt.legend()
# Personalizar la leyenda
plt.legend(loc='upper left', fontsize='small')
plt.show()"""


plt.hist(matematicas, bins=10)
plt.title('Distribución de las calificaciones de Matematicas')
plt.xlabel('Calificaciones de Matematicas')
plt.ylabel('Frecuencia')

plt.show()