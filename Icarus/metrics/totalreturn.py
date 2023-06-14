class TotalReturn:
    def __init__(self, initial_value, final_value):
        self.initial_value = initial_value
        self.final_value = final_value

    def calculate(self):
        total_return = ((self.final_value - self.initial_value) / self.initial_value)*100
        return total_return
