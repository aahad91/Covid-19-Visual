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
    bar=px.bar(x=nrw_data.age_group, y=nrw_data.cases, color=nrw_data.cases,
                color_continuous_scale=px.colors.sequential.YlGnBu, hover_data=[nrw_data.population],
                labels={'x':'Age Group', 'y':'Cases', 'hover_data_0':'Population'}).data[0]
    bar = go.Bar(x=nrw_data.age_group, y=nrw_data.cases)
    return nrw_data

def gp_bar_chart(data):
    #Suganthi
    df_nrw = data[data.state == 'Nordrhein-Westfalen']
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
    return bar_plots

    # title=go.layout.Title(text="Covid-19 Visualization in NRW county"),
    # yaxis_title="TOTAL CASES",
    # xaxis_title="COUNTY",
    # xaxis_tickvals=df_new.county,
    # xaxis_ticktext=tuple(df_new['county'].values)       
    # fig3 = go.Figure(data=bar_plots, layout=layt)
    # fig3.update_xaxes(rangeslider_visible=True)

#def scatter_plt(data):
    #Bhagyashree

def bubble_chart():
    #Sayalee
    data1 = pd.read_csv('data/covid_de.csv')
    data3 = pd.read_csv('data/counties_population.csv')
    pop=data1.loc[data1['state'] == 'Nordrhein-Westfalen']
    total_county = pop.county.unique()
    cases = []
    deaths = []
    recovered = []
    poulations = []
    for i in total_county:
        total_cases = 0
        total_deaths = 0
        total_recovered = 0
        cases_county=data1.loc[data1['county'] == i]
        for j in cases_county.cases:
            total_cases += j
        cases.append(total_cases)
        for k in cases_county.deaths:
            total_deaths += k
        deaths.append(total_deaths)
        for l in cases_county.recovered:
            total_recovered += l
        recovered.append(total_recovered)

    for m in total_county:
        pop_data = data3.loc[data3['county'] == m]
        for n in pop_data.population:
            poulations.append(n)

        
    df = pd.DataFrame() 
    df.insert(0, "county", total_county, True) 
    df.insert(1, "total_cases", cases, True) 
    df.insert(2, "total_deaths", deaths, True) 
    df.insert(3, "total_recovered", recovered, True) 
    df.insert(4, "population", poulations, True) 

    ratio = []
    for p in df.county:
        ratio_county=df.loc[df['county'] == p]
        ratio_s = float(ratio_county.total_cases/ratio_county.population)
        ratio.append(ratio_s) 

    df.insert(5, "ratio", ratio, True)
    return df

def dashboard(data1, data2):
    # for combining all plot and configuring dashbaord
    # Ahad
    # fig = make_subplots(
    #     rows=3, cols=2,
    #     specs= [[{"colspan": 2}, None], [{}, {}], [{}, {}]],
    #     subplot_titles=("First", "Second", "Third", "Forth", "Cases against Age Group")
    # )
    nrw_data = bar_chart(data1, data2)
    df = bubble_chart()


    fig = go.Figure()

    fig1 = go.Figure()
    fig2 = go.Figure()
    fig3 = go.Figure(data=gp_bar_chart(data1))
    
    #hi = go.Bar(x=nrw_data.age_group, y=nrw_data.cases,text="give some name here")
    # fig.add_trace(go.Bar(x=nrw_data.age_group, y=nrw_data.cases,visible=True))
    fig1.add_trace(go.Bar(x=nrw_data.age_group, y=nrw_data.cases,text="give some name here"))

    s=0
    for j in df.county:
        fig2.add_trace(go.Scatter(x=df.loc[df['county'] == j].population,
                y=df.loc[df['county'] == j].total_cases,
                name=j, text=j,
               # visible = False,              
                mode='markers',                 
                marker=dict(size=list(df.total_cases/15),color=s)
        ))
        s+= 1

    visible_arr = []
    visible_arr1 = []
    visible_arr2 = []
    visible_arr.append(True)
    visible_arr1.append(False)
    visible_arr2.append(False)

    # fig1.add_trace(fig1.data[0])
    # fig1.add_trace(fig1.data[0])
    fig.add_trace(fig1.data[0])
    g=0
    for m in df.county:
    #     print(g)
        fig.add_trace(fig2.data[g])
        g += 1
        visible_arr.append(False)
        visible_arr1.append(True)
        visible_arr2.append(False)
        
    fig.add_trace(fig3.data[0])
    visible_arr.append(False)
    visible_arr1.append(False)
    visible_arr2.append(True)
    fig.add_trace(fig3.data[1])
    visible_arr.append(False)
    visible_arr1.append(False)
    visible_arr2.append(True)
    fig.add_trace(fig3.data[2])
    visible_arr.append(False)
    visible_arr1.append(False)
    visible_arr2.append(True)
    
    # fig.update_layout(
    #     updatemenus=[
    #         dict(
    #             active=0,
    #             buttons=list([
                    
    #                 dict(label="By Age wise",
    #                     method="update",
    #                     args=[{"visible": visible_arr
                                
    #                             },{"title": "Cases By Age group"}]),
    #                 dict(label="By population",
    #                     method="update",
    #                     args=[{"visible": visible_arr1},
    #                         {"title": "Cases by Population"}]),
    #                 dict(label="By County wise",
    #                     method="update",
    #                     args=[{"visible": visible_arr2
                                
    #                             },{"title": "Cases by Counties NRW"}]),
                                
    #             ]),
    #         )
    #     ])
    # fig.add_trace(px.bar(x=nrw_data.age_group, y=nrw_data.cases, color=nrw_data.cases,
    #                 color_continuous_scale=px.colors.sequential.YlGnBu, hover_data=[nrw_data.population],
    #                 labels={'x':'Age Group', 'y':'Cases', 'hover_data_0':'Population'}).data[0])
    # fig.add_trace(, row=1, col=1)

    # fig.add_trace(, row=2, col=1)

    # fig.add_trace(, row=2, col=2)
    # df = bubble_chart()
    # s=0
    # for j in df.county:
    #     fig.add_trace(go.Scatter(x=df.loc[df['county'] == j].population,
    #             y=df.loc[df['county'] == j].total_cases,
    #             name=j, text=j,
    #             visible = True,               
    #             mode='markers',                 
    #             marker=dict(size=list(df.total_cases/15),color=s)
    #     ))
    #     s+= 1


    #fig.add_trace(go.Bar(x=barplt.age_group, y=barplt.cases), row=3, col=2)
    #fig.add_bar(x=barplt.age_group, y=barplt.cases, row=3, col=2)
   # fig.add_trace(bar_chart(data1, data2), row=3, col=2)
        # px.bar(x=barplt.age_group, y=barplt.cases, 
        #         color_continuous_scale=px.colors.sequential.YlGnBu, hover_data=[barplt.population],
        #         labels={'x':'Age Group', 'y':'Cases', 'hover_data_0':'Population'}).data[0], 
    #fig.update_xaxes(title_text="Age Group", row=3, col=2)
    #fig.update_yaxes(title_text="Total Cases", row=3, col=2)
    # fig.add_trace(go.Bar(x=nrw_data.age_group, y=nrw_data.cases, visible=False))
    # fig.update_layout(
    # updatemenus=[
    #     dict(
    #         active=0,
    #         buttons=list([
    #             dict(label="By Age wise",
    #                  method="update",
    #                  args=[{"visible": [True, False]},
    #                        {"title": "Yahoo",
    #                         }]),
    #             dict(label="By population",
    #                  method="update",
    #                  args=[{"visible": [False, True]},
    #                        {"title": "Yahoo High"}]),
                
    #         ]),
    #     )
    # ])

    #fig.update_layout(title_text="Nordrhein-Westfalen Covid-19 Dashboard")
    fig1.show()
    fig2.show()
    fig3.show()
    #fig.show()
# --------------------- #
if __name__ == "__main__":
    print("Hello Everyone!!")
    # variables
    # data1 -> covid_de.csv
    # data2 -> demographic_de.csv
    # Ahad
    data1 = pd.read_csv('data/covid_de.csv')
    data2 = pd.read_csv('data/demographics_de.csv')

    #bar_chart(data1, data2)
    dashboard(data1, data2)
    bubble_chart()