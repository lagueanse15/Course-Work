import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1
sns.boxplot(x = flight['hours'], y = flight['coach_price'], data = flight)
plt.show()
plt.clf()
## Task 2
sns.histplot(flight.coach_price[flight['hours'] == 8])
plt.ylabel('frequency')
plt.axvline(flight['coach_price'].mean())
plt.text(flight['coach_price'].mean(), 230,  'mean_coach_ticket_price')
plt.show()
plt.clf()

## Task 3
sns.histplot(flight.delay[flight.delay <= 20])
plt.show()
plt.clf()
sns.boxplot(flight.delay[flight.delay <= 15])
plt.show()
plt.clf()
print("flight delays seem to have a 10 minute average, the 25th percentile being 8 minutes and the 75th percentile being 11 minutes")
print("less likely delays that are outliers in the spread are from 0-4 minutes being not so notable delays and any delay after minutes is extremely unlikely")
## Task 4

perc = 0.1
flight_sub = flight.sample(n = int(flight.shape[0]*perc))
 
sns.lmplot(x = "coach_price", y = "firstclass_price", data = flight_sub, line_kws={'color': 'black'}, lowess=True)
plt.show()
plt.clf()


print("The price of a first class ticket is around 3-4x the price of a coach ticket for said flight based upon the visualiation of this graph")

## Task 5

sns.histplot(flight, x = 'coach_price', hue = flight.inflight_meal)
plt.show()
plt.clf()

sns.histplot(flight, x = 'coach_price', hue = flight.inflight_entertainment)
plt.show()
plt.clf()

sns.histplot(flight, x = 'coach_price', hue = flight.inflight_wifi)
plt.show()
plt.clf()

## Task 6
plt.scatter(x = flight.passengers, y = flight.hours, data = flight, alpha = 0.8)
plt.show()
plt.clf()
## Task 7
sns.lmplot(x ='coach_price', y='firstclass_price', hue = 'weekend', data = flight_sub, fit_reg= False)
plt.show()
plt.clf()
 
 
## Task 8
sns.boxplot(x = "day_of_week", y = "coach_price", hue = "redeye", data = flight)
plt.show()
plt.clf()





