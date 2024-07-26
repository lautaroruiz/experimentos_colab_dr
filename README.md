# Resultados experimentos colaborativos Labo I

## Experimento "Data Drifting" - Grupo B

Este repositorio fue creado con el objetivo de mostrar los resultados obtenidos de las corridas de experimentos diseñados para corregir el data drifting en variables monetarias.

Los métodos probados se corresponden con los subindices ev_{número}:
* EV_1: Ninguno
* EV_2: Rank Simple
* EV_3: Rank Cero Fijo
* EV_4: Deflación
* EV_5: Estandarizar
* EV_7: UVA
* EV_12: Dólar Blue 
* EV_13: Dólar Oficial Minorista

La notebook principal donde se generan los gráficos con los resultados de todas las corridas es:
* ganancia_exp_dr.ipynb

Además se incluyen:
* La carpeta 'metodos_nuevos': para obtener las series de "UVA", "dólar blue", "dólar oficial minorista".
* La carpeta 'semillero_custom':
    - 'data_scoring': archivos con los scores obtenidos con cada método ajustado y para cada semilla.
    - 'ganancia_semillero.ipynb': genera el modelo de "ensemble de semillas" para cada método.
* La carpeta 'data': contiene las ganancias para cada registro de la base de testing '202107' por semilla.