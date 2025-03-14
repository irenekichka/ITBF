from hw_2.base import Vehicle
from hw_2.engine import Engine

class Car(Vehicle):
    engine: Engine

    def __init__(self, weight, started, fuel, fuel_consumption, engine):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, obj):
        self.engine = obj   
