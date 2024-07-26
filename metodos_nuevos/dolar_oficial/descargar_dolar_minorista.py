## descarga serie mensual con la api del bcra

import requests
import pandas as pd
from datetime import datetime, timedelta

# "idVariable": 4,
# "cdSerie": 7927,
# "descripcion": "Tipo de Cambio Minorista ($ por USD) Comunicación B 9791 - Promedio vendedor",
# "fecha": "2024-07-25",
# "valor": 968.41


# Función para obtener datos desde la API en un rango de fechas
def obtener_datos_api(fecha_inicio, fecha_fin):
    url = f"https://api.bcra.gob.ar/estadisticas/v2.0/datosvariable/4/{fecha_inicio}/{fecha_fin}"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener datos: {response.status_code}")
        return None


datos1 = obtener_datos_api("2019-01-01", "2019-12-31")
datos1["results"]

datos2 = obtener_datos_api("2020-01-01", "2020-12-31")
datos2

datos3 = obtener_datos_api("2021-01-01", "2021-12-31")
datos3

# Extraer y concatenar los "results" de todos los diccionarios
df1 = pd.DataFrame(datos1["results"])
df2 = pd.DataFrame(datos2["results"])
df3 = pd.DataFrame(datos3["results"])
df_concatenado = pd.concat([df1, df2, df3], ignore_index=True)


# Convertir la columna 'fecha' a tipo datetime
df_concatenado["fecha"] = pd.to_datetime(df_concatenado["fecha"])

# Crear nuevas columnas para el año y el mes
df_concatenado["año_mes"] = df_concatenado["fecha"].dt.to_period("M")

# Agrupar por año y mes y calcular el promedio del valor
promedio_mensual = df_concatenado.groupby("año_mes")["valor"].mean().reset_index()

# Si quieres mostrarlo como un dataframe
promedio_mensual = promedio_mensual.rename(
    columns={"año_mes": "Mes", "valor": "Valor Promedio"}
)

print(promedio_mensual)
