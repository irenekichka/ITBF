from hw_2.base import Vehicle
from hw_2.exceptions import CargoOverload

class Plane(Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, weight, started, fuel, fuel_consumption, cargo, max_cargo):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, n):
        if n + self.cargo < self.max_cargo:
            self.cargo = self.cargo + n
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        n = self.cargo
        self.cargo = 0
        return n
