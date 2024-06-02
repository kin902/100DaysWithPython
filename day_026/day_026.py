# Exercise 28
"""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:
squared_numbers = [num * num for num in numbers]
# Write your code 👆 above:


print(squared_numbers)
"""

# Exercise 29
"""
list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:

result = [int(num) for num in list_of_strings if int(num) % 2 == 0]
# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"


# Write your code 👆 above:
print(result)
"""

"""""
# Exercise 30
with open("file1.txt") as data1:
    base_data = data1.readlines()
    base_data = [num.strip() for num in base_data]
with open("file2.txt") as data2:
    data3 = data2.readlines()
    data3 = [num.strip() for num in data3]
    result = [int(num.strip()) for num in base_data if num.strip() in data3]

# Write your code above 👆
print(result)
"""

"""
# exercise 41
sentence = input().split()
# 🚨 Don't change code above 👆
# Write your code below 👇
result = {word: len(word) for word in sentence}

print(result)
"""

weather_c = eval(input())
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# 🚨 Don't change code above 👆

# {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# Write your code 👇 below:
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}


print(weather_f)
