from hw_2.exceptions import LowFuelError, NotEnoughFuel

class Vehicle:
    started: bool = False
    weight: int = 1000
    fuel: float = 50.0
    fuel_consumption: float = 10.0

    def __init__(self, weight, started, fuel, fuel_consumption):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError
        else:
            raise exceptions.LowFuelError

    def move(self, distance):
        tmp = distance * self.fuel_consumption / 100.0
        if self.fuel >= tmp and self.started == True:
            self.fuel =  self.fuel - tmp
        else:
            raise exceptions.NotEnoughFuel

