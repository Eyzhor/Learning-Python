def get_average(scores):
    return sum(scores) / len(scores)

def print_student(name, scores):
    print(f"Name: {name}, Score: {scores}, Average: {get_average(scores)}")
    
def find_best_student(students):
    best_name = ""
    best_average = 0
    for name, scores in students.items():
        if get_average(scores) > best_average:
            best_average = get_average(scores)
            best_name = name
    return best_name 
    

students = {
    "Alice": [85, 92, 78],
    "Bob": [90, 88, 95],
    "Gabriel": [70, 75, 80]
}

for name, scores in students.items():
    print_student(name, scores)

best = find_best_student(students)
print(f"Best student: {best}")