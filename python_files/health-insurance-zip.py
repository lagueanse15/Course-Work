names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

insurance_costs.append(8320.0)
names.append("Priscilla")
print(insurance_costs)
print(names)

medical_records = (list(zip(insurance_costs, names)))
print(list(zip(insurance_costs, names)))

num_medical_records = len(medical_records)
print("There are",num_medical_records,"medical records")

first_medical_record = medical_records[0]
print("Here is the first medical record:",first_medical_record)

medical_records.sort()
print("Here are the medical records sorted by insurance cost: ", medical_records, '.')

cheapest_three = (medical_records[0:3])

print("Here are the three cheapest insurance costs in our medical records:", cheapest_three)

priciest_three =(medical_records[-3:])
print("Here are the three most expensive insurance costs in our medical records: ", priciest_three)

occurrences_paul = names.count("Paul")
print("There are", occurrences_paul, "individuals with the name Paul in our medical records. ")


"Here are the medical records sorted by insurance cost:", medical_records
# Add your code here
