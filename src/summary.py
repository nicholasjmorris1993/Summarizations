import re
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.offline import plot


def describe(df):
    model = Describe()
    model.statistics(df)
    model.plot(df)

    return model


class Describe:
    def statistics(self, df):
        self.stats = df.describe()

    def plot(self, df):
        fig = px.scatter_matrix(df, color=None, title="Pairs Plot")
        fig.update_traces(diagonal_visible=False)
        fig.update_layout(font=dict(size=16))
        plot(fig, filename="Pairs Plot.html")



