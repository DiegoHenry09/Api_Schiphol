from dotenv import load_dotenv
import os
import re
import requests
import time
import logging
from pathlib import Path
import pytz
import datetime 
from .constantes import BASE_URL 


# --- CARREGA O .env ---
# Adicionar esta linha torna o "dotenv run --" opcional
load_dotenv() 


# --- BLOCO 2: CONFIGURAÇÃO DO LOGGING ---
logging.basicConfig(
    filename="aeroporto.log", 
    format="%(asctime)s %(message)s",
    filemode="w"
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# --- BLOCO 3: FUNÇÕES PRINCIPAIS ---

def get_endpoint(endpoint, endpoint_id=None, params=None):
    
    headers = {
        "Accept": "application/json",
        "app_id": os.getenv("APP_ID"),
        "app_key": os.getenv("APP_KEY"),
        "ResourceVersion": "v4"
    }

    url = BASE_URL + endpoint

    if endpoint_id:
        url = url + "/" + endpoint_id

    
    resultados = []

    # --- Primeira Requisição ---
    logger.info(f"Buscando primeira página de: {url}")
    resultado_get = requests.get(url=url, headers=headers, params=params)
    resultado_get.raise_for_status() # Vai quebrar se a API falhar

    
    resultados.append(resultado_get.json())

    # Pega os headers da *primeira* requisição
    headers_da_resposta = resultado_get.headers
    numero_paginas = processar_headers_numero_paginas(headers_da_resposta)
    link = processar_headers_next(headers_da_resposta) 

    # Loop 'while' para processar as próximas páginas
    while link:
        time.sleep(0.5) # Respeita o limite da API
        logger.info(f"Buscando próxima página em: {link}")
        
        
        resultado_get = requests.get(url=link, headers=headers) 
        resultado_get.raise_for_status()

        
        resultados.append(resultado_get.json())

        
        link = processar_headers_next(resultado_get.headers)

    
    logger.info(f"Total de {len(resultados)} páginas recebidas com sucesso.")
    return resultados


def processar_headers_next(headers):
    headers_link = headers.get("link")

    if not headers_link:
        return None
    
    link_partes = headers_link.split(",")

    regular_exp = r"<(.*)>" # Captura a URL dentro de < >
    
    for link_parte in link_partes:
        if 'rel="next"' in link_parte:
            link = re.search(regular_exp, link_parte)
            if link:
                return link.groups()[0] # Retorna a URL

def processar_headers_numero_paginas(headers):

    headers_link = headers.get("link")

    if not headers_link:
        
        return 0
    
    link_partes = headers_link.split(",")
    
    
    exp_regular = r'page=([0-9]+)' 
    
    for parte in link_partes: 
        if 'rel="last"' in parte:
            match = re.search(exp_regular, parte) 
            
            if match:
                
                return int(match.group(1)) 
            
    
    return 0 




def get_flights_agendado_hoje():
    """Busca voos agendados para hoje."""
    return get_endpoint(endpoint="flights")

def get_flights_agendado_ontem():
   
    agora = datetime.datetime.now(pytz.timezone("Europe/Amsterdam"))
    ontem = agora.date() - datetime.timedelta(days=1)
    ontem = ontem.strftime("%Y-%m-%d")

    
    params = {"scheduleDate": ontem}
    logger.info(f"Buscando voos para data: {params}") 
    return get_endpoint(endpoint="flights", params=params)


def get_aircraft_types():
    """Busca os tipos de aeronaves."""
    return get_endpoint(endpoint="aircrafttypes")

def get_destinations():
    """Busca os destinos."""
    return get_endpoint(endpoint="destinations")

def get_destinations_por_iata(iata):
    return get_endpoint(endpoint='destinations', endpoint_id=iata)

def get_airlines():
    """BusCA as companhias aéreas."""
    return get_endpoint(endpoint="airlines")

def get_flight_por_id(fligth_id):
    return get_endpoint(endpoint='flights', endpoint_id=fligth_id)

def get_airline_por_iata_icao(iata_ou_icao):
    return get_endpoint(endpoint="airlines", endpoint_id=iata_ou_icao)
    
    
    
# Este bloco permite que o arquivo seja testado diretamente
if __name__ == "__main__":
    logger.info("Executando extrair.py como script de teste...")
    teste_airlines = get_airlines()
    logger.info(f"Teste: {len(teste_airlines)} páginas de companhias aéreas encontradas.")