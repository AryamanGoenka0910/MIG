class BaseStrategy:
    def __init__(self, data):
        self.data = data

    def generate_signals(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def plot_results(self):
        self.data[['price', 'signals']].plot(figsize=(10, 5))
