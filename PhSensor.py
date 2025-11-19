import random


class PhSensor:
    """Acts as a component of the system (Composition part)"""
    def __init__(self, precision=2):
        # Field to store the precision of the measurement (decimal places)
        self.precision = precision
        self.last_value = None

    def read_value(self):
        """Simulates reading data from the physical sensor (0-14 range)."""
        ph_value = random.uniform(0, 14)
        self.last_value = ph_value
        return round(ph_value, self.precision)
