
import requests
from bs4 import BeautifulSoup
import re

def remove_elements(arr_list, position):
    new_list = [arr for arr in arr_list if arr[position] != "0"]
    return new_list

# will give us a list of lists with basic upgrade information about a tower
def get_upgrade_data(url, name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') 
    
    # find the "table", if it is "None" that means we didn't find the info we are checking for from the url, and it will crash
    if url == "https://clashofclans.fandom.com/wiki/Town_Hall":
        tables = soup.find_all('table')
        if len(tables) >= 2:
            table = tables[6] # VERY spesific way to do this one url
    else:
        strings_to_check = ["wikitable", "wikitable floatheader row-highlight", "wikitable mode-toggle-mode-1"]
        table = soup.find(class_=strings_to_check)



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
                if 'bCost' in class_value:
                    upg_cost = cell.get_text()
                elif 'bTime' in class_value:
                    upg_time = cell.get_text()

        upg_level = str(upg_level).strip()
        upg_cost = str(upg_cost).strip()
        upg_time = str(upg_time).strip()

        upgrade_data.append([name, upg_level, upg_cost, upg_time])

    upgrade_data = remove_elements(upgrade_data, 1)
    
    return upgrade_data




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



