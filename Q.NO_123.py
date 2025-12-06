def classify(values):
    avg = sum(values) / len(values)
    if avg >= 80:
        return "Excellent"
    elif avg >= 60:
        return "On Track"
    elif avg >= 40:
        return "At Risk"
    else:
        return "Failing"

students = [
    {"name": "nikhil","attend":[89], "marks": [89, 90, 88]}, 
    {"name": "Ankith","attend":[75], "marks": [67, 65, 58]}, 
    {"name": "Neha","attend":[67], "marks": [56, 40, 42]}, 
    {"name": "Zara","attend":[45], "marks": [45, 30, 23]} 
]

for student in students:
    name = student["name"] 
    marks = student["marks"]
    attend = student["attend"]
    att = classify(attend)
    result = classify(marks)

    print(name,"'s result is: ", result,"and attendance is: ",att)