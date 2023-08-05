# with open("./weather_data.csv") as list:
#     data = list.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     temperatures = []
#     for row in data:
#         temperature.append(row[1])
#     for i in range(1, 8):
#         n = int(temperature[i])
#         temperatures.append(n)
# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# # data_dict = data.to_dict() #convert to dictionary
# # max_temp = data["temp"].max()
# # print(max_temp)
# # total_temp = 0
# # for i in temp_list:
# #     total_temp += i
# #
# # average_temp = total_temp / len(temp_list)
# # print(average_temp)
# # print(data[data.temp == max_temp])
# monday = data[data.day == "Monday"]
# temp = (monday.temp * 9/5) + 32
# print(temp)
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
list_fur_color_gray = data[data["Primary Fur Color"] == "Gray"]
list_of_gray = list_fur_color_gray["Primary Fur Color"].to_list()
list_fur_color_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
list_of_cinnamon = list_fur_color_cinnamon["Primary Fur Color"].to_list()
list_fur_color_black = data[data["Primary Fur Color"] == "Black"]
list_of_black = list_fur_color_black["Primary Fur Color"].to_list()
n_gray = len(list_of_gray)
n_cinnamon = len(list_of_cinnamon)
n_black = len(list_of_black)

squirrel_color_count = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [n_gray, n_cinnamon, n_black]
}
data = pandas.DataFrame(squirrel_color_count)
data.to_csv("squirrel_fur_count.csv")

