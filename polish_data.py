
from tabulate import tabulate

from data_functions import get_upgrade_data, convert_to_hours

import csv

# Put the raw data csv file name to polish
filename = 'raw_data_gold_defence.csv'

with open(filename, 'r') as file:
    reader = csv.reader(file)
    all_data = []
    for row in reader:
        all_data.append(row)





# Replace all invalid data with "-"
for i in range(len(all_data)):
    for j in range(len(all_data[i])):
        if all_data[i][j] == "None":
            all_data[i][j] = "-"


# make a "Hours" column
for elem in all_data:
    time_string = elem[3]
    if time_string != "-":
        time_hours = convert_to_hours(time_string)
        elem.append(time_hours)
    else:
        elem.append("-")


# convert the cost to a int value
for elem in all_data:
    cost_str = elem[2]
    if cost_str != "-":
        int_value = int(cost_str.replace(",", ""))
        elem[2] = int_value
    

# make a "cost/h" column
for elem in all_data:
    
    cost = elem[2]
    hours = elem[4]
    if cost != "-" and hours != "-":
        cost_pr_hour = round(elem[2] / elem[4])
        elem.append(cost_pr_hour)
    else:
        elem.append("-")



headers = ["Name", "Level", "Cost", "Time", "Time (hours)", "Cost/h"]

# Just to print in a pretty way
table = tabulate(all_data, headers, tablefmt="plain")
print(table)


#all_data.insert[0, headers]
all_data = [headers] + all_data

# Save the Polished Table
filename = "table_edit_me.csv"
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_data)

