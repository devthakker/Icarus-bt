class MaxDrawdown:
    def __init__(self, returns):
        self.returns = returns

    def calculate(self):
        peak = self.returns[0]
        drawdown = 0.0
        max_drawdown = 0.0

        for ret in self.returns:
            if ret > peak:
                peak = ret
                drawdown = 0.0
            else:
                drawdown = (peak - ret) / peak
                if drawdown > max_drawdown:
                    max_drawdown = drawdown

        return max_drawdown
