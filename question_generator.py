questions = []

# Easy
for i in range(1, 101):
    questions.append(f"easy|What is {i}+{i}?|{i+i}")

# Medium
for i in range(1, 101):
    questions.append(f"medium|What is {i}*2?|{i*2}")

# Hard
for i in range(1, 101):
    questions.append(f"hard|What is {i} squared?|{i*i}")

with open("questions.txt", "w") as f:
    for q in questions:
        f.write(q + "\n")

print("300 Questions Generated!")