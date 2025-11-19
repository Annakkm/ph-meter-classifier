class PhCaluculation:
    """Acts as a component of the system (Composition part)."""
    def __init__(self):
        # Fields defining the range for a neutral solution
        self.max_neutral = 6.9
        self.min_neutral = 7.1

    def get_type(self, ph_value):
        """Determines the type of solution (Acidic, Alkaline, or Neutral)."""
        if ph_value < self.min_neutral:
            return "Acid solution"
        elif ph_value > self.max_neutral:
            return "Alkaline solution"
        else:
            return "Neutral solution"

    def is_safe_for_drinking(self, ph_value):
        """Checks if the water is within safe drinking limits (6.5 - 8.5)."""
        return 6.5 <= ph_value <= 8.5
