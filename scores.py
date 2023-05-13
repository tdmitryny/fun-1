students_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}




students_grades = {}

for key in  students_scores:
    score = students_scores[key]
    if score > 90:
        students_grades[key] = "Outstanding"
    elif score > 80 and score < 90:
        students_grades[key] = "Exceed expectation"
    elif score > 70:
        students_grades[key] = "Acceptable"
    else:
        students_grades[key] = "Fail"


print(students_grades)
# students_scores["Harry"] = "Exceed expectation"
# students_scores["Ron"] = "Acceptable"
# students_scores["Hermione"] = "Outstanding"
# students_scores["Draco"] = "Acceptable"
# students_scores["Neville"] = "Fail"