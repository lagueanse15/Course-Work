medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""


num_records = 0

updated_medical_data = medical_data.replace("#","$")


for data in updated_medical_data:
  if data == "$":
    num_records += 1  

print("There are ", num_records, "medical records in the data")

medical_records = []

medical_data_split = []
medical_data_split = updated_medical_data.split(";")



for record in medical_data_split:
  medical_records.append(record.split(','))

medical_records_clean = []

for record in medical_records:
  record_clean = []

  for item in record:

    record_clean.append(item.strip())

  medical_records_clean.append(record_clean)
print(record_clean)
print(medical_records_clean)
names = []
ages = []
bmis = []
insurance_costs = []
for record in medical_records_clean:
  print(record[0])
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])
print("Names: ", names)
print("Ages: ", ages)
print("BMI: ", bmis)
print("Insurance Costs: ", insurance_costs)
total_bmi = 0



for bmi in bmis:
  total_bmi += float(bmi)
average_bmi = float(total_bmi)/8
print("The average bmi is:", average_bmi)
  




# Add your code here
