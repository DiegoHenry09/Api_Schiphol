from datetime import datetime, UTC, timezone


def atributos_para_dict(flight, lista_atributos):
    resultados = dict()

    for atributo in lista_atributos:
        resultados[atributo] = flight.get(atributo)

    return resultados


def atributos_data_para_dict(flight, lista_atributos):

    resultados = {}

    for atributo in lista_atributos:
        data = flight.get(atributo)
        
        if data:
            try:
                data = datetime.fromisoformat(data).astimezone(timezone.utc)
            except ValueError:
                data = None
        
        resultados[atributo] = data

    return resultados


def transformar_flights(flights_paginas):

    resultados = []

    flights = []

    for flight_pagina in flights_paginas:
        flights.extend(flight_pagina["flights"])

    for flight in flights:
        aircraftType = flight.get("aircraftType")

        aircraftType_iataMain = None
        aircraftType_iataSub = None
        if aircraftType:
            aircraftType_iataMain = aircraftType.get("iataMain")
            aircraftType_iataSub = aircraftType.get("iataSub")

        # rotas separadas por vírgula
        route = None
        eu = None
        visa = None
        flight_route = flight.get("route")
        if flight_route:
            destinations = flight_route.get("destinations")
            eu = flight_route.get("eu")
            visa = flight_route.get("visa")
            if destinations:
                route = ",".join(destinations)

        # codeshares separados por vírgula
        codeshares = None
        flight_codeshares = flight.get('codeshares')
        if flight_codeshares:
            flight_codeshares = flight_codeshares.get('codeshares')
            if flight_codeshares:
                codeshares = ",".join(flight_codeshares) 

        flight_states = None
        public_flight_states = flight.get("publicFlightState")
        if public_flight_states:
            flight_states = public_flight_states.get("flightStates")
            if flight_states:
                flight_states = ",".join(flight_states)

        atributos = {
            "aircraftType_iataMain": aircraftType_iataMain,
            "aircraftType_iataSub": aircraftType_iataSub,
            "route": route,
            "codeshares": codeshares,
            "flightStates": flight_states,
            "eu": eu,
            "visa": visa
        }





        atributos.update(
            atributos_para_dict(
                flight,
                [
                    "flightDirection",
                    "flightName",
                    "flightNumber",
                    "gate",
                    "pier",
                    "id",
                    "isOperationalFlight",
                    "mainFlight",
                    "prefixIATA",
                    "prefixICAO",
                    "airlineCode",
                    "aircraftRegistration",
                    "serviceType",
                    "terminal",
                ],
            )
        )

        atributos.update(
            atributos_data_para_dict(
                flight,
                [
                    "estimatedLandingTime",
                    "lastUpdatedAt",
                    "actualLandingTime",
                    "scheduleDateTime",
                    "actualOffBlockTime",
                    "expectedTimeBoarding",
                    "expectedTimeGateClosing",
                    "expectedTimeGateOpen",
                    "expectedTimeOnBelt",
                    "expectedSecurityFilter",
                    "publicEstimatedOffBlockTime",
                ],
            )
        )

        resultados.append(atributos)

    return resultados


def transformar_aircraft_types(aircraft_types_paginas):

    resultados = []
    aircraft_types = []

    for pagina in aircraft_types_paginas:
        aircraft_types.extend(pagina["aircraftTypes"])

    for aircraft in aircraft_types:
        resultados.append(
            {
                "iataMain": aircraft.get("iataMain"),
                "iataSub": aircraft.get("iataSub"),
                "description": aircraft.get("longDescription"),
            }
        )
    return resultados


def transformar_airlines(airlines_paginas):

    resultados = []
    airlines = []

    for pagina in airlines_paginas:
        airlines.extend(pagina.get("airlines"))

    for airline in airlines:
        resultados.append(
            {
                "iata": airline.get("iata"),
                "icao": airline.get("icao"),
                "nvls": airline.get("nvls"),
                "name": airline.get("publicName"),
            }
        )

    return resultados


def transformar_destinations(destinations_paginas):

    resultados = []
    destinations = []

    for pagina in destinations_paginas:
        destinations.extend(pagina.get("destinations"))

    for destination in destinations:

        name = destination.get("publicName")
        if name:
            name = name.get("english")

        resultados.append(
            {
                "name": name,
                "country": destination.get("country"),
                "iata": destination.get("iata"),
                "city": destination.get("city"),
            }
        )

    return resultados
