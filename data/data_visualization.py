# trading_framework/data/data_visualization.py

import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

class DataVisualization:

    def __init__(self):
        """
        Initialize the DataVisualization class
        """
        self.figure = None

    def visualize_vals(self, data, ticker, value='c', title=None):
        stock_close_data = data[value]
        plt.plot(stock_close_data.index, stock_close_data.values)

        plt.xlabel('Date')
        plt.ylabel('Price')

        if title is None:
            title=f'{ticker} Stock Prices'

        plt.title(title)
        plt.legend()

        self.figure = plt
        
        return plt
    

    def visualize_figure(self):
        """
        Show the currently stored figure if avaiable.
        """
        if self.figure:
            self.figure.show()
        else:
            print("No figure available to visualize. Run visualize_vals() first.")

    def save_figure(self, filename=None, format='png'):
        """
        Save the current figure to a file.
        filename: File name to save the plot (default is '{self.ticker}_Stock_Prices').
        format: File format for saving the figure (default is 'png').
        """

        if self.figure:
            if filename is None:
                filename = f'{self.ticker}_Stock_Prices.{format}'
            else:
                filename = f'{filename}.{format}'

            # Ensure valid file format
            if format not in ['png', 'jpg', 'pdf', 'svg']:
                raise ValueError("Invalid format. Please choose from 'png', 'jpg', 'pdf', or 'svg'.")

            self.figure.savefig(filename)
            print(f"Figure saved as {filename}")
        else:
            print("No figure available to save. Run visualize_vals() first.")