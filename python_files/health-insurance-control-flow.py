def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
   print("Smoking is not an issue for you.")
def analyze_children(children):
  if children >= 1:
    print("The insruance cost is high due to your number of dependents.")
  else:
   print("Your insurance isn't impacted much from your children")
# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name,"'s Estimated Insurance Cost: ", (estimated_cost), " dollars.")
  analyze_smoker(smoker)
  analyze_children(num_of_children)
  return estimated_cost
 
  
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)
