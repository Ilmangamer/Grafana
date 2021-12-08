import json
import time
from datetime import datetime 
import sys

# Accessing the files, without editing the file location
if len(sys.argv) < 3:
    print("Usage: butikkdata.py inputfil outputfil")
    sys.exit(1)

# Retrieving the today's date
Date_today= datetime.now().isoformat()
print(Date_today)

# Accessing the the files, without editing the file location
filename_for_txt = sys.argv[1] #"D:\VS Code\Python\Sublime\Grafana\Shop_data2.txt"


# Retrieving data from a txt file to a Python list
with open(filename_for_txt, "r") as pyopen:
    split = None
    my_split_list = []
    for split in pyopen.readlines():
        my_split_list.append(split.split())

my_split_list.append(split.split())

# I am iterating over each sublist in the list
# receiving the number strings, adding them together, then creating a dict out of it, and appending this dict in a new list

finished_new_data = []
for data in my_split_list:
    revenue = 0
    for each in data[1:]:
        try:
            conv_data = float(each)
            revenue +=conv_data
        except ValueError:
            print("error in value")
    new_dict={"Store": data[0], "Revenue": revenue, "Date": Date_today}
    finished_new_data.append(new_dict)

# Accessing the the files, without editing the file location
filename_for_json = sys.argv[2] #"D:\VS Code\Python\Sublime\Grafana\DBfGrafana2.json"

# To see what data is old, new and combined.
with open(filename_for_json, 'r') as f:
    old_data = json.loads(f.read())
    print(" -------- This is old data")
    print(old_data)
    print(" -------- This is new data"),
    print(finished_new_data),
    total_data = old_data + finished_new_data
    print(total_data)

# Dumps to json file
with open(filename_for_json, 'w') as fw:
    fw.write(json.dumps(finished_new_data))



   

      
