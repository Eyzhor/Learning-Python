students = {
    "Alice": [85, 92, 78],
    "Bob": [90, 88, 95],
    "Gabriel": [70, 75, 80]
}

for name, scores in students.items():
    average = sum(scores) / len(scores)
    print(f"{name}: {scores} — Average: {average}")

best_name = ""
best_average = 0

for name, scores in students.items():
    average = sum(scores) / len(scores)
    if average > best_average:
        best_average = average
        best_name = name
        
print(f"Highest Average: {best_name} - {best_average}")