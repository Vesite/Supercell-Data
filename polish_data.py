
from tabulate import tabulate

from data_functions import get_upgrade_data, convert_to_hours

import csv

# Replace all invalid data with "-"
#for i in range(len(all_data)):
#    for j in range(len(all_data[i])):
#        if all_data[i][j] == "None":
#            all_data[i][j] = "-"

def polish_data_func(all_data, do_print):

    # Make a "Hours" column
    for elem in all_data:
        time_string = elem[4]
        if time_string != "-":
            time_hours = convert_to_hours(time_string)
            elem.append(time_hours)
        else:
            elem.append("-")

    # Convert the cost to a int value
    for elem in all_data:
        cost_str = elem[3]
        if cost_str != "-":
            int_value = int(cost_str.replace(",", ""))
            elem[3] = int_value
        
    # Make a "cost/h" column
    for elem in all_data:
        cost = elem[3]
        hours = elem[5]
        if cost != "-" and hours != "-":
            cost_pr_hour = round(elem[3] / elem[5])
            elem.append(cost_pr_hour)
        else:
            elem.append("-")
    
    # Print in a pretty way
    headers = ["Name", "Tags", "Level", "Cost", "Time", "Time (hours)", "Cost/h"]
    if do_print:
        table = tabulate(all_data, headers, tablefmt="plain")
        print(table)

    # Return the data
    return [headers] + all_data







