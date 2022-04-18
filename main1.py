import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#plotting the graph
fig = ff.create_distplot([data],["Math Scores"], show_hist= False)
fig.show()