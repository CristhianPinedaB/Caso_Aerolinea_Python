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