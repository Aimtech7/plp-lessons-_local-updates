# plp = "academy"
# student_name = "Austine Makwaka"
# student_id = "123456789"
# student_age = 25.2
# Course_Name = "Web Development"
# Fees_clearance = True
# """student_details = {
#     "name": student_name,
#     "id": student_id,
#     "age": student_age,
#     "course": Course_Name,
#     "fees_clearance": Fees_clearance
# }
# print(f"Student Name: {student_details['name']}")
# print(f"Student ID: {student_details['id']}")   
# print(f"Student Age: {student_details['age']}")
# print(f"Course Name: {student_details['course']}")
# print(f"Fees Clearance: {student_details['fees_clearance']}")
# print(f"Path: {plp}/index.py")"""
# # This code snippet is a simple Python script that defines a student's details and prints them out. It also includes a path to the index.py file in the "academy" directory.
# print(student_name, student_id, student_age, Course_Name, Fees_clearance)
#creating a list
# languages = ["Python", "JavaScript",1995, "HTML", "CSS"]
# print(languages)
# shopping_list = ["Apples", "Bananas", "Oranges", "Grapes"]
# print(shopping_list)
# #Tuples
# fruits = ("Apple", "Banana", "Cherry")
# print(fruits)
#sets
# set_A = {1, 2, 3, 4, 5}
# set_B = {4, 5, 6, 7, 8}
# print(set_A)
# print(set_B)
#dictionaries
# student_details = {
#     "name": "Austine Makwaka",
#     "id": "123456789",
#     "age": 25.2,
#     "course": "Web Development",
#     "fees_clearance": True
# }
# print(student_details)
#logical operators
# a =10
# b = 20
# c = 30
# print(a < b and b < c)  # True
# print(a < b or b > c)   # True
# print(not (a > b))       # True
# print(a == 10 and b == 20)  # True  
# print(a != b or c > 25)  # True
# print(a < b and c > 25)  # True
# print(a > b or c < 35)  # True
# print(not (a < b))       # False
# print(a == 10 and b != 20)  # False
# print(a != 10 or b < 20)  # False

import random

jokes = [
    "Why do Python programmers wear glasses? Because they can't C!",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "How does a computer get drunk? It takes screenshots.",
    "Why do Java developers wear glasses? Because they don't see sharp.",
    "Why was the JavaScript developer sad? Because he didn't 'null' his feelings.",
    "Why did the Python function break up with the loop? It found closure.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer show up at work late? It had a hard drive.",
    "Why was the Python developer confused by the snake? It had no class.",
    "Why did the coder get kicked out of school? For taking classes literally!"
]

print("Here's a random programming joke for you! \n")
print(random.choice(jokes))