students_dict = {
    "Alice Doe": {"age": 20, "grades": [85, 90, 95]},
    "Bob Smith": {"age": 22, "grades": [88, 92, 90]},
    "Todd": {"age": 21, "grades": [80, 85, 78]},
}

todd_age = students_dict["Todd"]["age"]

print(todd_age)

todd_grades = students_dict["Todd"]["grades"][1]

print(todd_grades)
