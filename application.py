from typing import List, Dict
import random
import math

from model.Plane import Plane
from model.Ticket import Ticket
from model.Travel import Travel


# Funcion que crea una lista de aviones ----------------------------------------------------------------
def create_list_planes()->List[Plane]:
    planes_data = [
        {
            'code': 'A001',
            'economic_capacity': 24,
            'premium_capacity': 144,
        },
        {
            'code': 'A002',
            'economic_capacity': 24,
            'premium_capacity': 144
        },
        {
            'code': 'A003',
            'economic_capacity': 24,
            'premium_capacity': 144
        },
        {
            'code': 'A004',
            'economic_capacity': 24,
            'premium_capacity': 144
        }
    ]

    planes_list: List[Plane] = []

    # Iteramos la lista de aviones para instanciarlos
    for i, plane in enumerate(planes_data):
        obj_plane = Plane(str(plane['code']), int(plane['economic_capacity']), int(plane['premium_capacity']))
        planes_list.append(obj_plane)
    return planes_list
    

# Funcion que crea una lista de viajes de ida ----------------------------------------------------------------
def create_list_travels_outward()->List[Travel]:
    # Viajes de ida desde Lima a provincia
    outward_trips = [
        {
            'route': 'LIMA-AYACUCHO',
            'code_route': 'LIM-AYA',
            'base_price': 55.19,
            'economic_sales_min': 120,
            'economic_sales_max': 130,
            'premium_sales_min': 10,
            'premium_sales_max': 20
        },
        {
            'route': 'LIMA-CUSCO',
            'code_route': 'LIM-CUS',
            'base_price': 136.51,
            'economic_sales_min': 130,
            'economic_sales_max': 144,
            'premium_sales_min': 15,
            'premium_sales_max': 24
        },
        {
            'route': 'LIMA-AREQUIPA',
            'code_route': 'LIM-ARE',
            'base_price': 90.59,
            'economic_sales_min': 115,
            'economic_sales_max': 138,
            'premium_sales_min': 16,
            'premium_sales_max': 22
        },
        {
            'route': 'LIMA-TARAPOTO',
            'code_route': 'LIM-TAR',
            'base_price': 71.89,
            'economic_sales_min': 100,
            'economic_sales_max': 120,
            'premium_sales_min': 12,
            'premium_sales_max': 18
        }
    ]

    outward_trip_list:List[Travel] = []
    for i, travel in enumerate(outward_trips):
        object_travel = Travel(str(travel['route']), str(travel['code_route']), float(travel['base_price']), int(travel['economic_sales_min']), int(travel['economic_sales_max']), int(travel['premium_sales_min']), int(travel['premium_sales_max']))
        outward_trip_list.append(object_travel)
    
    return outward_trip_list

# Funcion que crea una lista de viajes de retorno ----------------------------------------------------------------
def create_list_travels_return()->List[Travel]:
    # Viajes de retorno de provincia a Lima
    return_trips = [
        {
            'route': 'AYACUCHO-LIMA',
            'code_route': 'AYA-LIM',
            'base_price': 40.42,
            'economic_sales_min': 100,
            'economic_sales_max': 115,
            'premium_sales_min': 10,
            'premium_sales_max': 15
        },
        {
            'route': 'CUSCO-LIMA',
            'code_route': 'CUS-LIM',
            'base_price': 124.32,
            'economic_sales_min': 105,
            'economic_sales_max': 120,
            'premium_sales_min': 14,
            'premium_sales_max': 20
        },
        {
            'route': 'AREQUIPA-LIMA',
            'code_route': 'ARE-LIM',
            'base_price': 86.59,
            'economic_sales_min': 100,
            'economic_sales_max': 110,
            'premium_sales_min': 13,
            'premium_sales_max': 18
        },
        {
            'route': 'TARAPOTO-LIMA',
            'code_route': 'TAR-LIM',
            'base_price': 68.42,
            'economic_sales_min': 90,
            'economic_sales_max': 105,
            'premium_sales_min': 10,
            'premium_sales_max': 15
        }
    ]

    return_trip_list:List[Travel] = []
    for i, travel in enumerate(return_trips):
        object_travel = Travel(str(travel['route']), str(travel['code_route']), float(travel['base_price']), int(travel['economic_sales_min']), int(travel['economic_sales_max']), int(travel['premium_sales_min']), int(travel['premium_sales_max']))
        return_trip_list.append(object_travel)
    
    return return_trip_list



# Función que crea una lista de Tickets de vuelo
def create_list_tickets(planes:List[Plane], travels_outward:List[Travel], travels_return:List[Travel])->List[Ticket]:
    list_tickets = []
    for i, travel in enumerate(planes):
        pass


# ---------- Funcion Principal ------------
def main():
    # Creamos la lista de aviones
    planes = create_list_planes()
    print(f"aviones --- {planes}")

    # Creamos la lista de viajes al día
    #travels = create_list_travels()
    #print(f"viajes --- {travels}")

    # Almacenamiento de tickets
    data_tickets = []
    
    
    


if __name__ == '__main__':
    main()