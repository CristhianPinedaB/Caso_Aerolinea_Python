
from typing import List, Dict
import random
import math
import operator

from model.Plane import Plane
from model.Ticket import Ticket
from model.Travel import Travel
from utils import create_tickets, create_list_trips_outward, create_list_trips_return, create_list_planes
from data import outward_trips, return_trips, planes_data


# --- Función que crea una lista de Tickets para cada vuelo -----
def create_list_tickets(trips_outward:List[Travel], trips_return:List[Travel])->List[Ticket]:
    # Unimos los viajes de ida y de retorno
    travels_joined = operator.add(trips_outward,trips_return)
    travels_tickets = []

    for i, travel in enumerate(travels_joined):
        tickets_created = create_tickets(travel)
        travels_tickets += tickets_created
    
    return travels_tickets



# ---------- Funcion Principal ------------
def main():
    # Creamos la lista de aviones
    planes = create_list_planes(planes_data)
    print(f"aviones --- {planes}")

    # Creamos la lista de vuelos de ida (Lima - Provincia)
    outward_travels = create_list_trips_outward(outward_trips, planes)
    print(f"viajes de ida --- {outward_travels}")

    # Creamos la lista de vuelos de retorno (Provincia - Lima)
    return_travels = create_list_trips_return(return_trips, planes)
    print(f"viajes de retorno --- {return_travels}")

    # Unimos los vuelos de ida y de retorno
    total_travels = outward_trips + return_trips
    print(f"total de viajes --- {len(total_travels)}")

    # Creamos los tickets de ida y vuelta
    total_tickets = create_list_tickets(outward_travels, return_travels)
    
    
    # Total de pasajes vendidos
    print(f"Número de pasajes vendidos = {total_tickets}")
    # Total de ingresos por la venta de pasajes economicos
    # Total de ingresos por la venta de pasajes premium
    # Total de IGV cobrado
    # Valor promedio de un pasaje Económico
    # Valor promedio de un pasaje Premium
    # Vuelo con mayor cantidad de pasajeros
    # Vuelo con menor cantidad de pasajeros
    # Tres primeros vuelos con mayor ingreso de venta de asiento
    # Avion con mayor cantidad de pasajeros
    


if __name__ == '__main__':
    main()