name1=input("Enter your name: ")
name2=input("Enter your crush's name: ")
score=0

for latter in name1.lower():
    score += name2.lower().count(latter)

for latter in name2.lower():
    score +=name1.lower().count(latter)

score %= 100

print(f"your compatibility score with {name2} is {score}%")