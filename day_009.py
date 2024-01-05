programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}
"""
# Exercise 22 day_009
print()
print("-------------------------------------------------------------------------------")
print("Exercise 22_day009")
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
student_s_scores = str()
# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    if 100 > student_scores[student] > 90:
        student_s_scores = "Outstanding"
    if 90 > student_scores[student] > 80:
        student_s_scores = "Exceeds Expectations"
    if 80 > student_scores[student] > 70:
        student_s_scores = "Acceptable"
    elif 70 > student_scores[student]:
        student_s_scores = "Fail"
    student_grades[student] = student_s_scores
# 🚨 Don't change the code below 👇
print(student_grades)
"""
# Exercise 23 day_009
print()
print("-------------------------------------------------------------------------------")
print("Exercise 23_day009")

country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = eval(input())  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(country_name, visits_time, list_of_cities_had_visit):
    new_country = {
        "country": country_name,
        "visits": visits_time,
        "cities": list_of_cities_had_visit
    }
    travel_log.append(new_country)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(type(travel_log))
print(travel_log)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
