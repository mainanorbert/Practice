from Data_handling import extract_json, extract_csv
import json
import csv


emp_file_name = "user_data_23_4.json"
vehicle_file_name = "user_data_23_4.csv"

employee_data = extract_json(emp_file_name)
vehicle_data = extract_csv(vehicle_file_name)

count = 0
for employee in employee_data:
     count += 1

count2 = 0
for vehicle in vehicle_data:
        count2 += 1

print(count, "employees" , "and", count2, "vehicles")

def combine(file_name):
    """
    checks for inconsistencies in the data user data and vehicle data if there are any inconsistencies it will remove the data from the list
    and return the combined data
    """
    with open(file_name + ".json", 'w', newline='') as combine:
        # writer = csv.writer(combine)
        # header = list(employee_data[0].keys())
        # header.extend(['Sex', 'Vehicle Make', 'Vehicle Model', 'Vehicle Year', 'Vehicle Type'])
        # writer.writerow(header)
        json_data = []
        for employee in range(len(employee_data)):
            First_Name = employee_data[employee]['firstName']
            Second_Name = employee_data[employee]['lastName']
            age = employee_data[employee]['age']

            for vehicle in range(len(vehicle_data)):
                if First_Name != vehicle_data[vehicle]['First Name'] and Second_Name != vehicle_data[vehicle]['Second Name'] and age != vehicle_data[vehicle]['Age (Years)']:
                    continue
                else:
                    employee_data[employee]['Sex'] = vehicle_data[vehicle]['Sex']
                    employee_data[employee]['Vehicle Make']= vehicle_data[vehicle]['Vehicle Make']
                    employee_data[employee]['Vehicle Model'] = vehicle_data[vehicle]['Vehicle Model']
                    employee_data[employee]['Vehicle Year'] = vehicle_data[vehicle]['Vehicle Year']
                    employee_data[employee]['Vehicle Type'] = vehicle_data[vehicle]['Vehicle Type']
                    # print(employee_data[employee])
                    # writer.writerow(employee_data[employee].values())
                    json_data.append(employee_data[employee])
                    break
        json.dump(json_data, combine, indent=4)
    return True                
                  

combine("combined_data")

def check_gender():
    ok = 0
    for data in vehicle_data:
        if data['Sex'] not in ['Male','Female']:
             print(data)
        else:
             ok += 1
    print(ok)
             
