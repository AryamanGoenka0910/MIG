# trading_framework/risk_management/risk_manager.py

class RiskManager:
    def __init__(self, max_position_size=0.1, max_drawdown=0.2):
        self.max_position_size = max_position_size  # As a fraction of total capital
        self.max_drawdown = max_drawdown

    def calculate_position_size(self, capital, price):
        position_size = (capital * self.max_position_size) // price
        return position_size

    def apply_stop_loss(self, portfolio, stop_loss_level):
        portfolio['stop_loss'] = portfolio['peak'] * (1 - stop_loss_level)
        portfolio['drawdown'] = (portfolio['peak'] - portfolio['total']) / portfolio['peak']
        return portfolio

    def check_risk(self, portfolio):
        if portfolio['drawdown'].min() < -self.max_drawdown:
            print("Max drawdown exceeded.")
            # TODO: Implement logic to stop trading or reduce positions
