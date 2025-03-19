
class LowFuelError(ValueError):
     """The exception should be used when the fuel level is low."""


class NotEnoughFuel(ValueError):
     """The exception should be used when there is not enough fuel."""


class CargoOverload(ValueError):
     """The exception should be used in case of cargo transhipment."""
