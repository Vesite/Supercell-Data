
import requests
from bs4 import BeautifulSoup
import re

# It's worth noting that the find_all() function returns a list of matching elements,
# while the find() function returns only the first matching element.
# If no elements match the given criteria, find_all() returns an empty list, while find() returns None.
# This is mentioned in tutorialspoint.com.



def remove_elements(arr_list, position):
    new_list = [arr for arr in arr_list if arr[position] != "0"]
    return new_list




# will give us a list of lists with basic upgrade information about a tower
def get_upgrade_data(url, name, tags):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') 
    
    raw_data_table = [] # List of lists (table)

    row_list = soup.find_all("tr") # row_list = All <td> objects in the HTML Code
    for row in row_list:
        cells = row.findChildren("td", recursive=False) # Check all the elements in the row (cells)
        for cell in cells:
            # Check if any of the cells have (class == "GoldPass bCost")
            if cell.has_attr("class"):# and ("GoldPass" in cell["class"]):
                if ('GoldPass' in cell["class"]) and (("rCost" in cell["class"]) or ("bCost" in cell["class"])): # Don't know why it finds nothing here when i put "'GoldPass rCost'"
                    
                    # Skip if first element is not level
                    if not (cells[0].get_text()).isdigit():
                        continue

                    upg_level = cells[0].get_text()

                    # Skip adding this "row" if we already have that level-value
                    for temp_row in raw_data_table:
                        if str(temp_row[2]) == str(upg_level).strip():
                            print("continued")
                            continue

                    upg_cost = "-"
                    upg_time = "-"

                    for cell in cells:
                        class_value = cell.get('class')
                        if class_value and 'GoldPass' in class_value:
                            if 'bCost' in class_value or 'rCost' in class_value:
                                upg_cost = cell.get_text()
                            elif 'bTime' in class_value or 'rTime' in class_value:
                                upg_time = cell.get_text()

                    upg_level = str(upg_level).strip()
                    upg_cost = str(upg_cost).strip()
                    upg_time = str(upg_time).strip()

                    row_data = [name, tags, upg_level, upg_cost, upg_time]
                    raw_data_table.append(row_data)





    return raw_data_table


    
    


"""
def basic_data_from_table(table, name):
    upgrade_data = []

    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 0:
            upg_level = cells[0].get_text()
        else:
            upg_level = 0
        upg_cost = None
        upg_time = None

        for cell in cells:
            class_value = cell.get('class')
            if class_value and 'GoldPass' in class_value:
                if 'bCost' in class_value or 'rCost' in class_value:
                    upg_cost = cell.get_text()
                elif 'bTime' in class_value or 'rTime' in class_value:
                    upg_time = cell.get_text()

        upg_level = str(upg_level).strip()
        upg_cost = str(upg_cost).strip()
        upg_time = str(upg_time).strip()

        upgrade_data.append([name, upg_level, upg_cost, upg_time])
    
    return upgrade_data
"""



# the "time_string" can look many different ways, always has "d", "h", "m", or "s" or a combination
def convert_to_hours(time_string):

    pattern_d = r'\d+(?=d)'
    match_d = re.findall(pattern_d, time_string)
    if len(match_d) > 0:
        days = match_d[0]
    else: days = 0

    pattern_h = r'\d+(?=h)'
    match_h = re.findall(pattern_h, time_string)
    if len(match_h) > 0:
        hours = match_h[0]
    else: hours = 0

    pattern_m = r'\d+(?=m)'
    match_m = re.findall(pattern_m, time_string)
    if len(match_m) > 0:
        minutes = match_m[0]
    else: minutes = 0

    pattern_s = r'\d+(?=s)'
    match_s = re.findall(pattern_s, time_string)
    if len(match_s) > 0:
        seconds = match_s[0]
    else: seconds = 0

    total_hours = float(days) * 24 + float(hours) + float(minutes)/60 + float(seconds)/3600

    return total_hours



