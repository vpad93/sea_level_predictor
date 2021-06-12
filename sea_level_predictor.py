import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',')

    # Create scatter plot
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(x = df['Year'], y=df['CSIRO Adjusted Sea Level'])
    years_series = pd.Series(range(1880,2051))
    plt.plot(years_series, res.intercept + res.slope * years_series, color = "red")


    # Create second line of best fit
    df_from_2000s = df[df['Year']>=2000]
    res_2 = linregress(df_from_2000s['Year'],df_from_2000s['CSIRO Adjusted Sea Level'])
    years_series_2 = pd.Series(range(2000,2051))
    plt.plot(years_series_2, res_2.intercept + res_2.slope * years_series_2, color = "green")

    # Add labels and title
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()