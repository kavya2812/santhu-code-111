import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

# #plotting the graph
fig = ff.create_distplot([data],["Math Scores"], show_hist= False)
# fig.show()

#calculating the mean and standard deviation of the population data
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean of popultion:- ",mean)
print("Standard deviation of popultion:- ",std_deviation)