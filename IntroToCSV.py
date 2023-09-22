# with open("weather_data.csv") as rawdata:
#     data = rawdata.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as raw_data:
#     data = csv.reader(raw_data)
#     #print(data)
#     new_list = []
#     weather_list = []
#     updated_list = []
#     for each_data in data:
#         new_list.append(each_data)
#     #print(new_list)
#     for item in new_list:
#         for i in range(len(item)):
#             if i == 1:
#                 weather_list.append(item[i])
#     #print(weather_list)
#     for weather in range(1,len(weather_list)):
#         updated_list.append(weather_list[weather])
#     #print(updated_list)
#     for i in range(0, len(updated_list)):
#         updated_list[i] = int(updated_list[i])
#     print(updated_list)

import pandas
print(pandas.read_csv("weather_data.csv"))

