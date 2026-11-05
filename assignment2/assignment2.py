import csv
import sys
import os
import custom_module
from datetime import datetime

#Task 02
def read_employees():
    employees = {}
    rows = []
    try:
        with open("../csv/employees.csv", newline="") as f:
            reader = csv.reader(f)
            first_row = True
            for row in reader:
                    if first_row:
                        employees["fields"] = row
                        first_row = False
                    else:
                        rows.append(row)
            employees["rows"] = rows

    except Exception as e:
        print(f"Exception: {e}")
        sys.exit(1)

    return employees

employees = read_employees()
print(employees)

#Tack 03
def column_index(column_name):
     return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

#Task 04
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

#Task 05
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Task 06
def employee_find_2(employee_id):
        matches = list(filter(lambda row : 
    int(row[employee_id_column]) == 
    employee_id , employees["rows"]))
        return matches

#Task 07
def sort_by_last_name():
     index = column_index("last_name")
     employees["rows"].sort(key=lambda row: row[index])
     return employees["rows"]

sort_by_last_name()
print(employees)

#Task 08
def employee_dict(row):
    result = {}
    for field, value in zip(employees["fields"], row):
        if field != "employee_id":
            result[field] = value
    return result

#Task 09
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        result[employee_id] = employee_dict(row)
    return result

print(all_employees_dict())

#Task 10
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("my new secret")
print(custom_module.secret)

#Task 12
def read_csv_as_dict(path):
    result = {}
    rows = []

    try:
        with open(path, newline="") as f:
            reader = csv.reader(f)
            first_row = True
            for row in reader:
                if first_row:
                    result["fields"] = row
                    first_row = False
                else:
                    rows.append(tuple(row))
            result["rows"] = rows
    except Exception as e:
        print(f"Exception: {e}")
        sys.exit(1)

    return result


def read_minutes():
    minutes1 = read_csv_as_dict("../csv/minutes1.csv")
    minutes2 = read_csv_as_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

#Task 13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()

#Task 14
def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

#Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list

sorted_minutes = write_sorted_list()
print(sorted_minutes)