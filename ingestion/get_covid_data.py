import requests
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.logger import get_logger

logger = get_logger("get_covid_data")

API_URL = "https://www.datos.gov.co/resource/gt2j-8ykr.json"

LIMIT = 50000
MAX_RECORDS = 1000000
OUTPUT_PATH = os.path.join("data", "raw", "covid_data.csv")

def get_data():
    all_data = []
    offset = 0

    logger.info("Iniciando descarga de datos desde la API...")

    while offset < MAX_RECORDS:
        params = {
            "$limit": LIMIT,
            "$offset": offset
        }

        response = requests.get(API_URL, params=params)

        if response.status_code != 200:
            logger.error(f"Error en la petición: {response.status_code} - {response.text}")
            break

        data_chunk = response.json()

        if not data_chunk:
            logger.info("No se recibieron más datos, finalizando descarga.")
            break

        all_data.extend(data_chunk)
        offset += LIMIT
        logger.info(f"Descargados {len(all_data)} registros...")

    # FINALIZA
    logger.info(f"Total de registros descargados: {len(all_data)}")

    # CREA EL DATAFRAME
    df = pd.DataFrame(all_data)
    # SINO EXISTE LA CREA
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # COLOCA EL ARCHIVO EN LA RUTA
    df.to_csv(OUTPUT_PATH, index=False)
    logger.info(f"Archivo guardado en: {OUTPUT_PATH}")

# INIT
if __name__ == "__main__":
    get_data()
