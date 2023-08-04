
from tabulate import tabulate

from data_functions import get_upgrade_data, convert_to_hours

import csv

# Will create some stats about a spesific building
# Average Cost/H and Total cost to max level

input_table_name = "Data - combined_tables_dark_elixir.csv"
result_table_name = "instance_data_dark_elixir.csv"


with open(input_table_name, 'r') as file:
        reader = csv.reader(file)
        input_table = []
        for row in reader:
            input_table.append(row)


# Find all rows with the same name

row_name_list = []
for row in input_table:
    row_name = row[0]
    if row_name not in row_name_list and row_name != "Name":
        row_name_list.append(row_name)



instance_stats_table = []

for name in row_name_list:
    total_cost = 0
    total_hours = 0
    total_upgrades = 0
    for row in input_table:
         if row[0] == name:
              total_upgrades += 1
              total_cost += int(row[2])
              total_hours += float(row[4])
    new_row = [name, total_upgrades, total_cost, round(total_hours), round(total_cost/total_hours)]
    instance_stats_table.append(new_row)

table = tabulate(instance_stats_table, tablefmt="plain")
print(table)

header = ["Name", "Total Upgrades", "Total Cost", "Total time (Hours)", "Gold/Hour"]
instance_stats_table = [header] + instance_stats_table

# Save the Instance Data
with open(result_table_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(instance_stats_table)










