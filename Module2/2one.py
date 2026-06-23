scores = []

for i in range(5):
    score = int(input(f"Enter score {i + 1}: "))
    scores.append(score)
    
print(f"Scores: {scores}")
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")
print(f"Average: {round(sum(scores) / len(scores), 2)}")