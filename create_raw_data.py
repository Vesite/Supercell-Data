from tabulate import tabulate
from data_functions import get_upgrade_data, convert_to_hours
import csv


# Create a CSV file from data scraped from some COC URL's
# Change "data_name_tail" and add some ULR's before running the script

all_data = []
data_name_tail = "gold_defence"


# Gold Defence
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Cannon/Home_Village", "Cannon"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Archer_Tower/Home_Village", "Archer Tower"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Mortar", "Mortar"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Air_Defense/Home_Village", "Air Defence"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Wizard_Tower", "Wizard Tower"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Air_Sweeper", "Air Sweeper"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Hidden_Tesla/Home_Village", "Hidden Tesla"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Bomb_Tower/Home_Village", "Bomb Tower"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/X-Bow/Home_Village", "A"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Inferno_Tower/Home_Village", "Inferno Tower"))

#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Eagle_Artillery", "Eagle Artillery"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Scattershot", "Scattershot"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Builder%27s_Hut", "Builder's Hut"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Spell_Tower", "Spell Tower"))

#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Town_Hall/Giga_Tesla", "Giga Telsa (TH12)"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Town_Hall/Giga_Inferno_(TH13)", "Giga Inferno (TH13)"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Town_Hall/Giga_Inferno_(TH14)", "Giga Inferno (TH14)"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Town_Hall/Giga_Inferno_(TH15)", "Giga Inferno (TH15)"))

# Gold Traps
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Bomb", "Bomb"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Spring_Trap/Home_Village", "Spring Trap"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Giant_Bomb", "Giant Bomb"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Air_Bomb", "Air Bomb"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Seeking_Air_Mine", "Seeking Air Mine"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Skeleton_Trap", "Skeleton Trap"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Tornado_Trap", "Tornado Trap"))

# Gold Town Hall
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Town_Hall", "Town Hall"))

# Gold Resources
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Elixir_Collector/Home_Village", "Elixir Collector"))
#all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Elixir_Storage/Home_Village", "Elixir Storage"))






# Save the Data Table
filename = "raw_data_" + data_name_tail + ".csv"
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_data)


# Print
headers = ["Name", "Level", "Cost", "Time"]
table = tabulate(all_data, headers, tablefmt="plain")
print(table)




