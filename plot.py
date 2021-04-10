import pandas as pd 
import plotly.express as px

df = pd.read_csv('CovidCases.csv')

fig = px.line(x = 'Date' y = 'Cases' color='Country' title='Covid Cases')
fig.show()