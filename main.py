from sch_phol_etl.extrair import (
    get_airlines, 
    get_destinations, 
    get_aircraft_types, 
    get_flights_agendado_ontem 
)
from sch_phol_etl.transformar import (
    transformar_airlines, 
    transformar_destinations, 
    transformar_aircraft_types, 
    transformar_flights
)
from sch_phol_etl.salvar import salvar
import logging
logger = logging.getLogger()


def main_etl():
    # --- EXTRACT (Extrair todos) ---
    logger.info("Iniciando ETL: Extração...")
    print("Iniciando ETL: Extração...")
    airlines_paginas = get_airlines()
    destinations_paginas = get_destinations()
    aircraft_paginas = get_aircraft_types()
    flights_paginas = get_flights_agendado_ontem() # Pega os voos de ontem

    # --- TRANSFORM (Transformar todos) ---
    logger.info("Iniciando ETL: Transformação...")
    print("Iniciando ETL: Transformação...")
    airlines = transformar_airlines(airlines_paginas)
    destinations = transformar_destinations(destinations_paginas)
    aircraft_types = transformar_aircraft_types(aircraft_paginas)
    flights = transformar_flights(flights_paginas)

    # --- LOAD (Salvar todos) ---
    logger.info("Iniciando ETL: Carregamento (Salvando)...")
    print("Iniciando ETL: Carregamento (Salvando)...")
    
    #  UMA lista de planilhas e UMA lista de nomes
    salvar(
        dir_arquivos=".", 
        planilhas=[airlines, destinations, aircraft_types, flights], 
        planilhas_nomes=["airlines", "destinations", "aircraft_types", "flights"]
    )
    
    logger.info("ETL Concluído!")
    print("ETL Concluído!")

    
    
if __name__ == "__main__":
    main_etl()