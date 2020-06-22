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

# ---Task Functions --- #


#def multi_line_chart(data):
    #Bhagyashree

#def bar_chart(data):
    #Ahad

#def gp_bar_chart(data):
    #Suganthi

#def scatter_plt(data):
    #Bhagyashree

#def bubble_chart(data1, data2):
    #Sayalee

#def dashboard(data1, data2):
    # for combining all plot and configuring dashbaord
    # Ahad
# --------------------- #
if __name__ == "__main__":
    print("Hello Everyone!!")
    # variables
    # data1 -> covid_de.csv
    # data2 -> demographic_de.csv
    # Ahad
    data1 = pd.read_csv('data/covid_de.csv')
    print(data1.head())

    data2 = pd.read_csv('data/demographics_de.csv')
    print(data2.head())
