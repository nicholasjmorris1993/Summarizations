import pandas as pd
import sys
sys.path.append("/home/nick/Summarizations/src")
from summary import describe


data = pd.read_csv("/home/nick/Summarizations/test/LungCap.csv")

metrics = describe(data)

metrics.stats
