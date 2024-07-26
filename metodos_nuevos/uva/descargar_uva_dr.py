## descarga serie mensual con la api del bcra

import requests
import pandas as pd
from datetime import datetime, timedelta


# Función para obtener datos desde la API en un rango de fechas
def obtener_datos_api(fecha_inicio, fecha_fin):
    url = f"https://api.bcra.gob.ar/estadisticas/v2.0/datosvariable/31/{fecha_inicio}/{fecha_fin}"
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


promedio_mensual["var%"] = (
    promedio_mensual.loc[promedio_mensual["Mes"] == "2020-12", "Valor Promedio"].iloc[0]
    / promedio_mensual["Valor Promedio"]
)


promedio_mensual["var%"].to_list()

# 202012


vfoto_mes = [
    201901,
    201902,
    201903,
    201904,
    201905,
    201906,
    201907,
    201908,
    201909,
    201910,
    201911,
    201912,
    202001,
    202002,
    202003,
    202004,
    202005,
    202006,
    202007,
    202008,
    202009,
    202010,
    202011,
    202012,
    202101,
    202102,
    202103,
    202104,
    202105,
    202106,
    202107,
    202108,
    202109,
]

vIPC = [
    1.9903030878,
    1.9174403544,
    1.8296186587,
    1.7728862972,
    1.7212488323,
    1.6776304408,
    1.6431248196,
    1.5814483345,
    1.4947526791,
    1.4484037589,
    1.3913580777,
    1.3404220402,
    1.3154288912,
    1.2921698342,
    1.2472681797,
    1.2300475145,
    1.2118694724,
    1.1881073259,
    1.1693969743,
    1.1375456949,
    1.1065619600,
    1.0681100000,
    1.0370000000,
    1.0000000000,
    0.9680542110,
    0.9344152616,
    0.8882274350,
    0.8532444140,
    0.8251880213,
    0.8003763543,
    0.7763107219,
    0.7566381305,
    0.7289384687,
]

pd.DataFrame({"fecha": vfoto_mes, "valor": vIPC})
