"""
Assignment-5: Covid-19 Visualization
Group-11
Members: Abdul Ahad Ayaz, Sayalee Chavan, Suganthi Jaganathan,
Bhagyashree Sanjay Borade
"""

# ---packages--- #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import warnings
# ---Task Functions --- #
warnings.simplefilter("ignore")

#def multi_line_chart(data):
    #Bhagyashree

def bar_chart(data1, data2):
    #Ahad
    
    return bar
def gp_bar_chart(data2):
    #Suganthi
#Preprocessing the data
    df_nrw = data2[data2.state == 'Nordrhein-Westfalen']
    df_nrw.fillna(method='pad')
    df_nrw['age_group']=df_nrw['age_group'].str.replace('-','_')
    df_new=df_nrw.groupby(['county'])["cases", "deaths","recovered"].apply(lambda x : x.astype(int).sum()).reset_index()
    #Visualizing the data
    x = df_new['county']
    bar_plots = [
        go.Bar(x=x, y=df_new['cases'], name='Confirmed cases', marker=go.bar.Marker(color='#FFA07A')),
        go.Bar(x=x, y=df_new['deaths'], name='Deaths', marker=go.bar.Marker(color='#C71585')),
        go.Bar(x=x, y=df_new['recovered'], name='Recovered cases', marker=go.bar.Marker(color='#0000FF'))

    ]
    layt = go.Layout(
        title=go.layout.Title(text="Covid-19 Visualization in NRW county"),
        yaxis_title="TOTAL CASES",
        xaxis_title="COUNTY",
        xaxis_tickvals=df_new.county,
        xaxis_ticktext=tuple(df_new['county'].values),
    )       
    fig = go.Figure(data=bar_plots, layout=layt)
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()
    return fig

#def scatter_plt(data):
    #Bhagyashree

#def bubble_chart(data1, data2):
    #Sayalee

def dashboard(data1,data2):
    
# --------------------- #
    if __name__ == "__main__":
        
        gp_bar_chart(data2)
        
    # variables
    # data1 -> covid_de.csv
    # data2 -> demographic_de.csv
    # Ahad

#    
     

#    bar_chart(data1, data2)
data1 = pd.read_csv('data\covid_de.csv')
data2 = pd.read_csv('data\demography.csv')    
dashboard(data1,data2)
