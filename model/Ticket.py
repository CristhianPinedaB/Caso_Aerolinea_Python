from typing import List, Dict
from config import IGV, ECONOMIC_PRICE_OUTWARD, ECONOMIC_PRICE_RETURN, PREMIUM_PRICE
from model.Plane import Plane
from model.Travel import Travel


class Ticket(object):

    def __init__(self, number:int, travel:Travel, seat_type:str):
        self.number = number
        self.travel = travel
        self.seat_type = seat_type
        self.calculate_amounts()

    def __repr__(self) -> str:
        return self.seat_type

    # falta saber como sabemos si es de ida o vuelta para calcular precio
    def calculate_amounts(self)->None:
        # Validamos si el vuelo es de Lima a provincia
        if self.travel.code_route[:3] == 'LIM':
            if self.seat_type == 'economic':
                self.seat_price = ECONOMIC_PRICE_OUTWARD
            else:
                self.seat_price = PREMIUM_PRICE
            self.subtotal = round(self.travel.base_price + self.seat_price, 2)
            self.igv = round(self.subtotal*IGV/100, 2)
            self.total = round(self.subtotal + self.igv, 2)
        # Validamos si el vuelo es de provincia a Lima
        else:
            if self.seat_type == 'economic':
                self.seat_price = ECONOMIC_PRICE_RETURN
            else:
                self.seat_price = PREMIUM_PRICE
            self.subtotal = round(self.travel.base_price + self.seat_price, 2)
            self.igv = round(self.subtotal*IGV/100, 2)
            self.total = round(self.subtotal + self.igv, 2)
            
        