
def maria_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for ", name ," is, ", estimated_cost, "dollars.")
  difference = (estimated_cost - 1000)
  print("The difference in insurance cost is ", difference, " dollars.")
  return estimated_cost

maria_insurance_cost('Maria', 28, 0, 26.2, 3, 0)


# Initial variables for Maria 
age = 28
sex = 0  
bmi = 26.2
num_of_children = 3
smoker = 0  

# Estimate Maria's insurance cost
def omar_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for ", name ," is  ", insurance_cost,  " dollars.")
maria_insurance_cost('Omar', 35, 1, 22.2, 0, 1)
# Initial variables for Omar
age = 35
sex = 1 
bmi = 22.2
num_of_children = 0
smoker = 1  

# Estimate Omar's insurance cost 
