from PhSensor import PhSensor
from PhCalculation import PhCaluculation


class PhMeter:
    """Implements the Composition principle ('Has-a' relationship)."""
    def __init__(self):
        # The PHMeter 'has a' sensor and 'has a' classifier
        self.sensor = PhSensor()
        self.calculation = PhCaluculation()
        self.last_measurement = None

    def analyze_ph(self):
        # Using the sensor component to get data
        # ph_value = self.sensor.read_value()
        ph_value = 7.09
        # Using the classifier component
        solution_type = self.calculation.get_type(ph_value)
        is_potable = self.calculation.is_safe_for_drinking(ph_value)

        # Storing results in a dictionary
        self.last_measurement = {
            'ph': ph_value,
            'type': solution_type,
            'potable': is_potable
        }
        return self.last_measurement

    def print_results(self):
        """Displays the results to the console."""
        print("\n---- Analysis result ----")
        print(f"Ph level: {self.last_measurement['ph']}")
        print(f"Ph type: {self.last_measurement['type']}")
        # Convert boolean to Yes/No string
        safety_liquid = 'Yes' if  self.last_measurement['potable'] else 'No'
        print(f"Drinkable: {safety_liquid}")
