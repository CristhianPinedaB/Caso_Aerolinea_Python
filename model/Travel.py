

class Travel(object):

    def __init__(self, route: str, code_route: str, base_price: float, economic_sales_min: int, economic_sales_max: int, premium_sales_min:int, premium_sales_max:int):
        self.route = route
        self.code_route = code_route
        self.base_price = base_price
        self.economic_sales_min = economic_sales_min
        self.economic_sales_max = economic_sales_max
        self.premium_sales_min = premium_sales_min
        self.premium_sales_max = premium_sales_max
    
    def __repr__(self) -> str:
        return self.code_route
