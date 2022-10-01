import random
import math

from typing import List
from model.Ticket import Ticket
from model.Travel import Travel
from model.Plane import Plane



# -------------Funcion que crea una lista de aviones ----------------------------------------------------------------
def create_list_planes(planes_data)->List[Plane]:

    planes_list: List[Plane] = []

    # Iteramos la lista de aviones para instanciarlos
    for i, plane in enumerate(planes_data):
        obj_plane = Plane(str(plane['code']), int(plane['economic_capacity']), int(plane['premium_capacity']))
        planes_list.append(obj_plane)
    return planes_list


# -----------Funcion que crea una lista de viajes de ida ----------------------------------------------------------------
def create_list_trips_outward(outward_trips, planes_data)->List[Travel]:
    # Viajes de ida desde Lima a provincia
    outward_trip_list:List[Travel] = []
    for i, travel in enumerate(outward_trips):
        object_travel = Travel(str(planes_data[i]), str(travel['route']), str(travel['code_route']), float(travel['base_price']), int(travel['economic_sales_min']), int(travel['economic_sales_max']), int(travel['premium_sales_min']), int(travel['premium_sales_max']))
        outward_trip_list.append(object_travel)
    
    return outward_trip_list


# ---------Funcion que crea una lista de viajes de retorno ----------------------------------------------------------------
def create_list_trips_return(return_trips, planes_data)->List[Travel]:
    # Viajes de retorno de provincia a Lima
    return_trip_list:List[Travel] = []
    for i, travel in enumerate(return_trips):
        object_travel = Travel(str(planes_data[i]) ,str(travel['route']), str(travel['code_route']), float(travel['base_price']), int(travel['economic_sales_min']), int(travel['economic_sales_max']), int(travel['premium_sales_min']), int(travel['premium_sales_max']))
        return_trip_list.append(object_travel)
    
    return return_trip_list



# ------ Funcion que crea tickets -------
def create_tickets(travel:Travel):
    tickets_premium_economic = []
    number_ticket = 0

    # Creamos tickets con asiento Premium
    for i in range(random.randint(travel.premium_sales_min, travel.premium_sales_max)):
        number_ticket+=1
        object_ticket_eco = Ticket(int(number_ticket), travel, str('premium'))
        #print(f"objeto - {object_ticket_eco}")
        tickets_premium_economic.append(object_ticket_eco)

    # Creamos tickets con asiento Economico
    for i in range(random.randint(travel.economic_sales_min, travel.economic_sales_max)):
        number_ticket+=1
        object_ticket_prem = Ticket(int(number_ticket), travel, str('economic'))
        #print(f"objeto - {object_ticket_prem}")
        tickets_premium_economic.append(object_ticket_prem)
    
    return tickets_premium_economic


# ----- Funcion que retorna los tickets por vuelo -----
def tickets_per_travel(list_tickets: List[Ticket], code_route):
    tickets_filtered = [ticket for ticket in list_tickets if ticket.travel.code_route == code_route]
    return len(tickets_filtered)


# --- Funcion que retorna el numero de pasajeros por avion -----
def tickets_per_plane(list_tickets: List[Ticket], plane_code):
    tickets_filtered = [ticket for ticket in list_tickets if ticket.travel.plane.code == plane_code]
    return len(tickets_filtered)


# --- Funcion que retorna el avion con mayor pasajeros ---
def plane_max_passenger(list_tickets: List[Ticket], list_planes: List[Plane]):
    list_obj = []
    for i, plane in enumerate(list_planes):
        number_tickets = tickets_per_plane(list_tickets, plane['code'])
        tickets_plane = {'number_tickets': number_tickets, 'plane': plane['code']}
        list_obj.append(tickets_plane)
    
    list_ordered = sorted(list_obj, key=lambda d: d['number_tickets'])
    return list_ordered


# ---- Funcion que ordena de mayor a menor el numero de pasajeros por vuelo ----
def order_list_tickets(list_tickets: List[Ticket], list_travels: List[Travel]):
    list_obj = []
    for i, travel in enumerate(list_travels):
        number_tickets = tickets_per_travel(list_tickets, travel['code_route'])
        tickets_route = {'number_tickets': number_tickets, 'route': travel['route']}
        list_obj.append(tickets_route)
    
    list_ordered = sorted(list_obj, key=lambda d: d['number_tickets'])
    return list_ordered

