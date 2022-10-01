
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

    # Numero de tickets Economicos
    number_eco = len([ticket for ticket in total_tickets if ticket.seat_type == 'economic'])

    # Numero de tickets Premium
    number_prem = len([ticket for ticket in total_tickets if ticket.seat_type == 'premium'])

    
    print("-------------------------------------------------------")
    
    # Total de pasajes vendidos
    print(f"Numero de pasajes vendidos al dia: {len(total_tickets)}")

    # Total de ingresos por la venta de pasajes economicos
    total_incomes_eco = round(sum([ticket.total for ticket in total_tickets if ticket.seat_type == 'economic']),2)
    print(f"Total de ingresos por la venta de pasajes Economicos: ${total_incomes_eco}")
    
    # Total de ingresos por la venta de pasajes premium
    total_incomes_prem = round(sum([ticket.total for ticket in total_tickets if ticket.seat_type == 'premium']),2)
    print(f"Total de ingresos por la venta de pasajes Premium: ${total_incomes_prem}")
    
    # Total de IGV cobrado
    total_igv = round(sum([ticket.igv for ticket in total_tickets]),2)
    print(f"Total de IGV cobrado: ${total_igv}")

    # Valor promedio de un pasaje Económico
    value_avg_eco = round((sum([ticket.total for ticket in total_tickets if ticket.seat_type == 'economic']))/number_eco, 2)
    print(f"Valor promedio de un pasaje Economico: ${value_avg_eco}")

    # Valor promedio de un pasaje Premium
    value_avg_prem = round((sum([ticket.total for ticket in total_tickets if ticket.seat_type == 'premium']))/number_prem, 2)
    print(f"Valor promedio de un pasaje Premium: ${value_avg_prem}")
    # Vuelo con mayor cantidad de pasajeros
    # Vuelo con menor cantidad de pasajeros
    # Tres primeros vuelos con mayor ingreso de venta de asiento
    # Avion con mayor cantidad de pasajeros
    


if __name__ == '__main__':
    main()