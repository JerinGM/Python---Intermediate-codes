# with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as data:
#     content = data.read()
#     print(content)
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Dataframe - print(squirrel_data)
data = squirrel_data["Primary Fur Color"]
gray = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
cinnamon = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
#print(data)
# my_csv = data.value_counts()
# print(my_csv.to_csv("new.csv"))
print(gray)
print(black)
print(cinnamon)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [2473, 392, 103]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv("Jerins.csv")