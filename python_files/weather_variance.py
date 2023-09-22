import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

london_data 
print(london_data.head(5))
print(len(london_data))

temp = london_data["TemperatureC"]
print(temp)
average_temp = np.mean(temp)
print("The average temperature in london during 2015 is:", average_temp)
temperature_var = np.var(temp)
print("The variance of temperature in london during 2015 is:", temperature_var)

temperature_standard_deviation = np.std(temp)
print("The standard deviation of temperature is: ", temperature_standard_deviation)
print(london_data.head())
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
print(june)
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]
june_mean = np.mean(june)
print("The mean for the month of june is:", june_mean)
july_mean = np.mean(july)
print("The mean for the month of july is:", july_mean)
sdjune = np.std(june)
print("The standard deviation for the month of june is:", sdjune)
sdjuly = np.std(july)
print("The standard deviation for the month of july is:", sdjuly)

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month ", str(i), " is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month ", str(i), " is "+ str(np.std(month)) +"\n")

