"""
import csv

with open("./weather_data.csv") as data_file:

    data = csv.reader(data_file)
    weather = []

    for row in data:
        if row[1] != "temp":
            weather.append(int(row[1]))
            
    print(weather)
"""
import pandas
"""
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
print(data.to_dict())

temp_list = data["temp"].to_list()
print(temp_list)

print(data["condition"])
or
print(data.condition)

print(data["temp"].mean())
print(data["temp"].max())

print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])
"""

squirrel_data = pandas.read_csv("Squirrel_Data_2018-2024.csv")

grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

print(grey_squirrels_count)
print(black_squirrels_count)
print(cinnamon_squirrels_count)

data_dict = {
    "Fur_color": ["Gray", "black", "Cinnamon"],
    "Count": [grey_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
