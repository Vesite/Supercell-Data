from tabulate import tabulate
from data_functions import get_upgrade_data, convert_to_hours
import csv


# Create a CSV file from data scraped from some COC WIKI URL's
# Change "data_name_tail" and add some ULR's before running the script

all_data = []
data_name_tail = "temp"


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




"""

# Elixir Resources
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Gold_Mine/Home_Village", "Gold Collector"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Gold_Storage/Home_Village", "Gold Storage"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Dark_Elixir_Drill", "Dark Elixir Drill"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Dark_Elixir_Storage", "Dark Elixir Storage"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Clan_Castle", "Clan Castle"))

# Elixir Army Buildings
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Army_Camp/Home_Village", "Army Camp"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Barracks", "Barracks"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Dark_Barracks", "Dark Barracks"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Laboratory", "Labratory"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Spell_Factory", "Spell Factory"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Dark_Spell_Factory", "Dark Spell Factory"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Workshop", "Workshop"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Pet_House", "Pet House"))

# Elixir Hero
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Grand_Warden", "Grand Warden"))

# Elixir Army
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Barbarian", "Barbarian", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Archer", "Archer", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Giant", "Giant", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Goblin", "Goblin", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Wall_Breaker", "Wall Breaker", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Balloon", "Balloon", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Wizard", "Wizard", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Healer", "Healer", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Dragon", "Dragon", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/P.E.K.K.A", "P.E.K.K:A", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Baby_Dragon/Home_Village", "Baby Dragon", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Miner", "Miner", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Electro_Dragon", "Electro Dragon", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Yeti", "Yeti", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Dragon_Rider", "Dragon Rider", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Electro_Titan", "Electro Titan", True))

# Elixir Siege Machines
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Wall_Wrecker", "Wall Wrecker", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Battle_Blimp", "Battle Blimp", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Stone_Slammer", "Stone Slammer", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Siege_Barracks", "Siege Barracks", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Log_Launcher", "Log Launcher", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Flame_Flinger", "Flame Flinger", True))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Battle_Drill", "Battle Drill", True))

# Elixir Spells
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Lightning_Spell/Home_Village", "Lightning Spell"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Healing_Spell/Home_Village", "Healing Spell"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Rage_Spell/Home_Village", "Rage Spell"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Jump_Spell/Home_Village", "Jump Spell"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Freeze_Spell", "Freeze Spell"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Clone_Spell", "Clone Spell"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Invisibility_Spell", "Invisibility Spell"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Recall_Spell", "Recall Spell"))








# Dark Elixir Hero
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Barbarian_King", "Barbarian King"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Archer_Queen", "Archer Queen"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Royal_Champion", "Royal Champion"))

# Dark Elixir Army
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Minion", "Minion"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Hog_Rider", "Hog Rider"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Valkyrie", "Valkyrie"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Golem", "Golem"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Witch", "Witch"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Lava_Hound", "Lava Hound"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Bowler", "Bowler"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Ice_Golem", "Ice Golem"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Headhunter", "Headhunter"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Apprentice_Warden", "Apprentice Warden"))



all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Poison_Spell", "Posion Spell"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Earthquake_Spell", "Earthquake Spell"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Haste_Spell", "Haste Spell"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Skeleton_Spell", "Skeleton Spell"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Bat_Spell", "Bat Spell"))


# Dark Elixir Pets
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/L.A.S.S.I", "L.A.S.S.I"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Electro_Owl", "Electro Owl"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Mighty_Yak", "Mighty Yak"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Unicorn", "Unicorn"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Frosty", "Frosty"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Diggy", "Diggy"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Poison_Lizard", "Posion Lizard"))
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Phoenix", "Phoenix"))

# Dark Elixir Defence
all_data.extend(get_upgrade_data("https://clashofclans.fandom.com/wiki/Monolith", "Monolith"))

"""


# Save the Data Table
filename = "raw_data_" + data_name_tail + ".csv"
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_data)


# Print
headers = ["Name", "Level", "Cost", "Time"]
table = tabulate(all_data, headers, tablefmt="plain")
print(table)




