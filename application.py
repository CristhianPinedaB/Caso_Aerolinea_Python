
from typing import List, Dict
import random
import math
import operator

from model.Plane import Plane
from model.Ticket import Ticket
from model.Travel import Travel
from utils import create_tickets, create_list_trips_outward, create_list_trips_return, create_list_planes, tickets_per_travel, order_list_tickets, plane_max_passenger
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

    # Creamos la lista de vuelos de ida (Lima - Provincia)
    outward_travels = create_list_trips_outward(outward_trips, planes)

    # Creamos la lista de vuelos de retorno (Provincia - Lima)
    return_travels = create_list_trips_return(return_trips, planes)

    # Unimos los vuelos de ida y de retorno
    total_travels = outward_trips + return_trips

    # Creamos los tickets de ida y vuelta
    total_tickets = create_list_tickets(outward_travels, return_travels)

    # Numero de tickets Economicos
    number_eco = len([ticket for ticket in total_tickets if ticket.seat_type == 'economic'])

    # Numero de tickets Premium
    number_prem = len([ticket for ticket in total_tickets if ticket.seat_type == 'premium'])

    # Vuelos ordenados por numero de pasajeros
    ordered_travels = order_list_tickets(total_tickets, total_travels)

    # Avion ordenados por numero de pasajeros
    #ordered_planes = plane_max_passenger(total_tickets, planes)

    print('\n')
    print("--------------------------------------------------------------------")
    print("--------------------- REPORTE DIARIO AEROLINEA ---------------------")
    print("--------------------------------------------------------------------")
    print('\n')
    # Numero de pasajess por vuelo
    print('> Numero de pasajes por vuelo:')
    print(f" - Lima -> Ayacucho: {tickets_per_travel(total_tickets, 'LIM-AYA')}")
    print(f" - Lima -> Cusco: {tickets_per_travel(total_tickets, 'LIM-CUS')}")
    print(f" - Lima -> Arequipa: {tickets_per_travel(total_tickets, 'LIM-ARE')}")
    print(f" - Lima -> Tarapoto: {tickets_per_travel(total_tickets, 'LIM-TAR')}")
    print(f" - Ayacucho -> Lima: {tickets_per_travel(total_tickets, 'AYA-LIM')}")
    print(f" - Cusco -> Lima: {tickets_per_travel(total_tickets, 'CUS-LIM')}")
    print(f" - Arequipa -> Lima: {tickets_per_travel(total_tickets, 'ARE-LIM')}")
    print(f" - Tarapoto -> Lima: {tickets_per_travel(total_tickets, 'TAR-LIM')}")
    # Total de pasajes vendidos
    print(f"> Numero de pasajes vendidos al dia: {len(total_tickets)}")

    print('\n')
    # Total de ingresos por la venta de pasajes economicos
    total_incomes_eco = round(sum([ticket.total for ticket in total_tickets if ticket.seat_type == 'economic']),2)
    print(f"> Total de ingresos por la venta de pasajes Economicos: ${total_incomes_eco}")
    
    # Total de ingresos por la venta de pasajes premium
    total_incomes_prem = round(sum([ticket.total for ticket in total_tickets if ticket.seat_type == 'premium']),2)
    print(f"> Total de ingresos por la venta de pasajes Premium: ${total_incomes_prem}")
    
    # Total de IGV cobrado
    total_igv = round(sum([ticket.igv for ticket in total_tickets]),2)
    print(f"> Total de IGV cobrado: ${total_igv}")

    print('\n')
    # Valor promedio de un pasaje Económico
    value_avg_eco = round((sum([ticket.total for ticket in total_tickets if ticket.seat_type == 'economic']))/number_eco, 2)
    print(f"> Valor promedio de un pasaje Economico: ${value_avg_eco}")

    # Valor promedio de un pasaje Premium
    value_avg_prem = round((sum([ticket.total for ticket in total_tickets if ticket.seat_type == 'premium']))/number_prem, 2)
    print(f"> Valor promedio de un pasaje Premium: ${value_avg_prem}")

    # Vuelo con mayor cantidad de pasajeros
    print(f"> Vuelo con mayor cantidad de pasajeros: {ordered_travels[len(total_travels)-1]['route']}")

    # Vuelo con menor cantidad de pasajeros
    print(f"> Vuelo con menor cantidad de pasajeros: {ordered_travels[0]['route']}")

    print('\n')
    # Tres primeros vuelos con mayor ingreso de venta de asiento
    print('> Tres primeros vuelos con mayor ingreso de venta de asiento:')
    for i in range(3):
        print(f"- {ordered_travels[len(total_travels)-1-i]['route']}: {ordered_travels[len(total_travels)-1-i]['number_tickets']} pasajes")

    # Avion con mayor cantidad de pasajeros
    #print(f"Avion con mayor cantidad de pasajeros: {ordered_planes[len(total_travels)-1]['plane']}")
    
    print('\n')
    print("--------------------------------------------------------------------")


if __name__ == '__main__':
    main()