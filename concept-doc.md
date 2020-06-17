# Assignment 5 - Covid-19

### Concept Document

### Group-11

#### Members: Abdul Ahad Ayaz, Sayalee Chavan, Suganthi Jaganathan, Bhagyashree Sanjay Borade

This document provides the overview of our project, containing the description of dataset, the End Users that we are targeting, visualization techniques that we are going to use and in the end how can we explore the visulaized data using different intreraction techniques. 

------

### DATA

(Assigned: Abdul Ahad Ayaz)

There are two datasets that we are going to use **covid_de.csv** and **demgraphics_de.csv**. First dataset **covid_de.csv** provides the daily update of Covid-19 cases of different states and counties of Germany based on gender and age group. Second dataset **demgraphics_de.csv** is the supporting dataset for the first dataset as it contains the population of different states of Germany based on gender and age group. The reason of choosing these dataset upon other dataset is that it satisfies the requirement of End User described below.

##### Data Source

- **covid_de.csv**
  - https://www.kaggle.com/headsortails/covid19-tracking-germany (covid_de.csv is refined dataset based on RKI data)
  - https://npgeo-corona-npgeo-de.hub.arcgis.com (Collected by [Robert Koch Institute](https://www.rki.de/EN/Home/homepage_node.html))
- **demographic_de.csv**
  - https://www-genesis.destatis.de/genesis/online/data?operation=sprachwechsel&language=en (Collected by [Statistisches Bundesamt](https://www.destatis.de/EN/Home/_node.html))

##### Dataset Type

| Dataset                | Spatial vs Non-Spatial Data | Point, Scalar, Vector Data |
| ---------------------- | --------------------------- | -------------------------- |
| **covid_de.csv**       | Non-Spatial Data            | Point Data                 |
| **demographic_de.csv** | Non-Spatial Data            | Point Data                 |

##### Dataset Characteristics

The first dataset **covid_de.csv** consist of following columns:

| Column Name   | Data    Type | Description                                                  |
| ------------- | ------------ | ------------------------------------------------------------ |
| **state**     | Nominal      | It contains the name of German states that are total 16 in number. Example Baden-Wuerttemberg, Nordrhein-Westfalen, Hessen, Bayern etc. |
| **county**    | Nominal      | It contains the name of counties of each state label with LandKries(LK)/StadtKries(SK). Example SK Koeln, SK Hamm, LK Paderborn, LK Guetersloh in Nordrhein-Westfalen state. |
| **age_group** | Ordinal      | It consists of different age categories such as 0-4, 5-14, 15-34, 35-59, 60-79, 80-99 and empty field NA with age unknown. |
| **gender**    | Ordinal      | it consist of gender M for male and F for female and NA for gender unknown. |
| **date**      | Nominal      | it consist of date when the data is updated.                 |
| **cases**     | Quantitative | it consist of per day count of confirmed cases of Covid-19.  |
| **deaths**    | Quantitative | it consits of per day count of death due to Covid-19         |
| **recovered** | Quantitative | it consists of per day count of recovered patients from Covid-19. |

The Second file **demographics_de.csv** that we are going to use for our project consist of following columns: 

| Column Name    | Data Type    | Description                                                  |
| -------------- | ------------ | ------------------------------------------------------------ |
| **state**      | Nominal      | It contains the name of German states that are total 16 in number. Example Baden-Wuerttemberg, Nordrhein-Westfalen, Hessen, Bayern etc. |
| **gender**     | Ordinal      | It consist of gender such as male and female.                |
| **age_group**  | Ordinal      | It consists of different age categories such as 0-4, 5-14, 15-34, 35-59, 60-79 and 80-99. |
| **population** | Quantitative | It consists of population categorized by state, gender and age. |

##### Data Modeling

- **covid_de.csv** is described as Entity <img src="https://render.githubusercontent.com/render/math?math=E_6^P">, where P represents that dataset has Point Data and 6 represents the dimensions.
- **demographics_de.csv** is described as Entity <img src="https://render.githubusercontent.com/render/math?math=E_3^P">, where P represents that dataset has Point Data and 3 represents the dimensions.



### USER AND TASK

(Assigned: Suganthi Jaganathan)



### VISUALIZATION TECHNIQUES

(Assigned: Bhagyashree Sanjay Borade)

### INTERACTIONS

(Assigned: Sayalee Chavan)

Interaction in visualization techniques provides more understanding of visual representation. User can do the selection, filtering for switching between different visualization techniques or choosing data variables.
Interaction for visualization techniques specified as following:

-  **Filtering/ Range slider:**
   With the use of range slider, the user can select a particular range for days mentioned on the x-axis as well as able to see cases in the range of selected days. This technique can be used in Multi-Series line chart.

-  **Selection:**
   Selection can be used for visualizing different data variables by clicking/unclicking on it and selection will be one or multiple. This interaction operator can be used in Multi-Series Line Chart where the user can do selection based on "No. of confirmed cases", "No. of recovered cases" and "No. of deaths". For Bar Chart(3D) and Grouped Bar Chart(3D), the user can select between Bar Chart and Grouped Bar Chart. For Grouped Bar Chart(3D), visualization can be customized by selecting checkboxes represents "No. of confirmed cases", "No. of recovered cases" and "No. of deaths".  For Scatter plot multi-series, User can customize the visualization by selecting the checkbox in legends based on gender(male/ female). For Bubble Chart, User can customize visualization by selecting the checkbox which consists of "Total confirmed cases", "No. of recovered cases", "No. of deaths" parameters.

- **Hover:**