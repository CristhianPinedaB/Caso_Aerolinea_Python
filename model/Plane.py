
class Plane(object):

    def __init__(self, code:str, economic_capacity:int, premium_capacity:int):
        self.code = code
        self.economic_capacity = economic_capacity
        self.premium_capacity = premium_capacity
        self.total_capacity = economic_capacity + premium_capacity

    def __repr__(self) -> str:
        return self.code