from tabulate import tabulate
from data_functions import get_upgrade_data, convert_to_hours
from polish_data import polish_data_func
import csv


# Create a CSV file from data scraped from some COC URL's
# Change "data_name_tail" and add some ULR's before running the script

all_data = []




all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Cannon/Home_Village", "Cannon", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Archer_Tower/Home_Village", "Archer Tower", ["Gold", "Defence"]))

#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Wizard_Tower", "Wizard Tower", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Elixir_Collector/Home_Village", "Elixir Collector", ["Gold", "Resource", "Collector"]))



all_data = polish_data_func(all_data, True)





# Save the Polished Table
data_file_name_tail = "test_example_2"
filename = "new_data_table_" + data_file_name_tail + ".csv"
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_data)

