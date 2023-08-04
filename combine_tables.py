





from tabulate import tabulate

from data_functions import get_upgrade_data, convert_to_hours

import csv

# Put the raw data csv file name to polish
result_filemane = "combined_tables_dark_elixir.csv"
# table_filenames = ["table_elixir_army.csv", "table_elixir_army_buildings.csv", "table_elixir_grand_warden.csv", "table_elixir_resources.csv", "table_elixir_siege_machines.csv", "table_elixir_spells.csv"]
# table_filenames = ["table_gold_defence.csv", "table_gold_resources.csv", "table_gold_th.csv", "table_gold_traps.csv"]
table_filenames = ["table_dark_elixir_army.csv", "table_dark_elixir_defence.csv", "table_dark_elixir_hero.csv", "table_dark_elixir_pets.csv", "table_dark_elixir_spells.csv"]
result_table = []

for filename in table_filenames:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        all_data = []
        for row in reader:
            all_data.append(row)
        
        result_table.extend(all_data)





# Just to print in a pretty way
print(result_table)


# Save the Combined Table
with open(result_filemane, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(result_table)


