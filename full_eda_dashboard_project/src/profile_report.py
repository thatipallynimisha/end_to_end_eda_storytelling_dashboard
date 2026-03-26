
from ydata_profiling import ProfileReport
import pandas as pd

df = pd.read_csv('../data/data.csv')
profile = ProfileReport(df)
profile.to_file("../reports/profile.html")
