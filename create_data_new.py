from tabulate import tabulate
from data_functions import get_upgrade_data, convert_to_hours
from polish_data import polish_data_func
import csv


# Create a CSV file from data scraped from some COC URL's
# Change "data_name_tail" and add some ULR's before running the script

all_data = []


"""

# Gold Defence
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Cannon/Home_Village", "Cannon", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Archer_Tower/Home_Village", "Archer Tower", ["Gold", "Defence"]))

all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Mortar", "Mortar", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Air_Defense/Home_Village", "Air Defence", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Wizard_Tower", "Wizard Tower", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Air_Sweeper", "Air Sweeper", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Hidden_Tesla/Home_Village", "Hidden Tesla", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Bomb_Tower/Home_Village", "Bomb Tower", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/X-Bow/Home_Village", "X-Bow", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Inferno_Tower/Home_Village", "Inferno Tower", ["Gold", "Defence"]))

all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Eagle_Artillery", "Eagle Artillery", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Scattershot", "Scattershot", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Builder%27s_Hut", "Builder's Hut", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Spell_Tower", "Spell Tower", ["Gold", "Defence"]))

all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Town_Hall/Giga_Tesla", "Giga Telsa (TH12)", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Town_Hall/Giga_Inferno_(TH13)", "Giga Inferno (TH13)", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Town_Hall/Giga_Inferno_(TH14)", "Giga Inferno (TH14)", ["Gold", "Defence"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Town_Hall/Giga_Inferno_(TH15)", "Giga Inferno (TH15)", ["Gold", "Defence"]))

# Gold Trap
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Bomb", "Bomb", ["Gold", "Trap"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Spring_Trap/Home_Village", "Spring Trap", ["Gold", "Trap"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Giant_Bomb", "Giant Bomb", ["Gold", "Trap"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Air_Bomb", "Air Bomb", ["Gold", "Trap"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Seeking_Air_Mine", "Seeking Air Mine", ["Gold", "Trap"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Skeleton_Trap", "Skeleton Trap", ["Gold", "Trap"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Tornado_Trap", "Tornado Trap", ["Gold", "Trap"]))

# Gold Town Hall
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Town_Hall", "Town Hall", ["Gold", "Town Hall"]))

# Gold Resource
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Elixir_Collector/Home_Village", "Elixir Collector", ["Gold", "Resource"]))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Elixir_Storage/Home_Village", "Elixir Storage", ["Gold", "Resource"]))

"""


all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Bomb", "Bomb", ["Gold", "Trap"]))

all_data = polish_data_func(all_data, True)





# Save the Polished Table
data_file_name_tail = "test_delete_me"
filename = "new_data_table_" + data_file_name_tail + ".csv"
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_data)

