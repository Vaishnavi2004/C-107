import csv
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data.csv")

student = df.loc[df['student_id'] == "TRL_abc"] #.loc filter out all the rows with given student id

print(student.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x = student.groupby("level")["attempt"].mean(),
    y = ['level 1','level 2','level 3','level 4'],
    orientation = 'v'))

fig.show()
