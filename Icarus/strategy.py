

class strategy:
    """
    Base class for all strategies.
    """
    def __init__(self, optimize=False, optimize_range=range(1, 20)):
        self.optimize = optimize
        self.optimize_range = optimize_range

    def check_for_buy(self, line):
        pass
    
    def check_for_sell(self, line):
        pass
    
    