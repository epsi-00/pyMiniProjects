print("Welcome to my Computer Quiz!")

playing = input("Do you want to play? ")

print(playing)

while playing != "yes":
    print("Please answer with 'yes' to play the game.")
    playing = input("Do you want to play? ").lower()
    if playing == "no":
        print("Okay, maybe next time!")
        quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Central Processing Unit'.")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Graphics Processing Unit'.")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct')
    score += 1
else:
    print("Incorrect! The correct answer is 'Graphics Processing Unit'.")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Graphics Processing Unit'.")
    print("Incorrect!")

print(f"Game Over! Your score: {score}")
print("You got " + str((score / 4) * 100) + "%.")

if score == 5:
    print("Perfect!")
elif score <= 1:
    print("I think you need to study..")
else:
    print("Very Good!")


