import logging

class strategy:
    """
    Base class for all strategies.
    """
    def __init__(self, optimize=False, optimize_range=range(1, 20), logging=False):
        self.optimize = optimize
        self.optimize_range = optimize_range
        if logging:
            self.logger = logging.getLogger(__name__)

    def check_for_buy(self, line):
        pass
    
    def check_for_sell(self, line):
        pass
    
    