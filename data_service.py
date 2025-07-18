# data_service.py
import os
import mysql.connector
import pandas as pd

config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
}

def obtener_conexion():
    return mysql.connector.connect(**config)

def obtener_resultados_historicos():
    cnx = obtener_conexion()
    cursor = cnx.cursor()

    query = """
    SELECT fecha, equipo_local, equipo_visitante, goles_local, goles_visitante
    FROM resultados
    WHERE fecha < CURDATE()
    """

    cursor.execute(query)
    filas = cursor.fetchall()

    columnas = ['fecha', 'equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante']
    df = pd.DataFrame(filas, columns=columnas)

    cursor.close()
    cnx.close()

    return df

if __name__ == "__main__":
    df = obtener_resultados_historicos()
    print(df.head())
