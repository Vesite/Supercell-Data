




# find all the rows in the table
rows = upgrade_costs.find_all('tr')
# iterate over each row
for row in rows:
    # find all the cells in the row
    cells = row.find_all('td')
    
    # extract the data from each cell
    data = [cell.get_text() for cell in cells]
    
    # print the extracted data
    print(data)



# Iterate over each row
for row in rows:
    # Find all the cells in the row
    cells = row.find_all('td')
    
    # Extract the data from each cell
    data = [cell.get_text() for cell in cells]
    
    # Print the extracted data
    print(data)





gold_pass_bcost = None
gold_pass_btime = None

for cell in cells:
    if 'class="GoldPass bCost"' in cell:
        gold_pass_bcost = cell
    elif 'class="GoldPass bTime"' in cell:
        gold_pass_btime = cell

data.append([gold_pass_bcost, gold_pass_btime])




for cell in cells:
    if cell.get("class_") == "GoldPass bCost":
        upg_cost = cell.get_text()
    elif cell.get("class") == "GoldPass bTime":
        upg_cost = cell.get_text()