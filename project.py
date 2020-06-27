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
# ---Task Functions --- #


#def multi_line_chart(data):
    #Bhagyashree

def bar_chart(data1, data2):
    #Ahad
    #print(data)
    nrw_data = data1[data1.state == 'Nordrhein-Westfalen']
    nrw_data.fillna(method='pad', inplace=True)
    nrw_data.age_group = nrw_data.age_group.str.replace('-', '_') 
    nrw_data = nrw_data.groupby('age_group')['cases'].apply(lambda x : x.sum()).reset_index()

    pop = data2[data2.state == 'Nordrhein-Westfalen']
    pop.age_group = pop.age_group.str.replace('-', '_')
    pop = pop.groupby('age_group')['population'].apply(lambda x : x.sum()).reset_index()
    nrw_data['population'] = pop['population']
     # fig = px.bar(nrw_data, x='age_group', y='cases', color='cases', color_continuous_scale=px.colors.sequential.YlGnBu)
    # fig.update_layout(title="Cases against Age Group", xaxis_title="Age Group", yaxis_title="Total Cases")
    # fig.show()
    bar=px.bar(x=nrw_data.age_group, y=nrw_data.cases,
                color_continuous_scale=px.colors.sequential.YlGnBu, hover_data=[nrw_data.population],
                labels={'x':'Age Group', 'y':'Cases', 'hover_data_0':'Population'}).data[0]
    return bar
#def gp_bar_chart(data):
    #Suganthi

#def scatter_plt(data):
    #Bhagyashree

#def bubble_chart(data1, data2):
    #Sayalee

def dashboard(data1, data2):
    # for combining all plot and configuring dashbaord
    # Ahad
    fig = make_subplots(
        rows=3, cols=2,
        specs= [[{"colspan": 2}, None], [{}, {}], [{}, {}]],
        subplot_titles=("First", "Second", "Third", "Forth", "Cases against Age Group")
    )

    # fig.add_trace(, row=1, col=1)

    # fig.add_trace(, row=2, col=1)

    # fig.add_trace(, row=2, col=2)

    # fig.add_trace(, row=3, col=1)


    #fig.add_trace(go.Bar(x=barplt.age_group, y=barplt.cases), row=3, col=2)
    #fig.add_bar(x=barplt.age_group, y=barplt.cases, row=3, col=2)
    fig.add_trace(bar_chart(data1, data2), row=3, col=2)
        # px.bar(x=barplt.age_group, y=barplt.cases, 
        #         color_continuous_scale=px.colors.sequential.YlGnBu, hover_data=[barplt.population],
        #         labels={'x':'Age Group', 'y':'Cases', 'hover_data_0':'Population'}).data[0], 
    fig.update_xaxes(title_text="Age Group", row=3, col=2)
    fig.update_yaxes(title_text="Total Cases", row=3, col=2)


    fig.update_layout(title_text="Nordrhein-Westfalen Covid-19 Dashboard")
    fig.show()
# --------------------- #
if __name__ == "__main__":
    print("Hello Everyone!!")
    # variables
    # data1 -> covid_de.csv
    # data2 -> demographic_de.csv
    # Ahad
    data1 = pd.read_csv('data/covid_de.csv')
    data2 = pd.read_csv('data/demographics_de.csv')

    bar_chart(data1, data2)
    dashboard(data1, data2)