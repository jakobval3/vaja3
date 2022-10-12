import random
import json


secret = random.randint(1, 30)
print(secret)
attempts = 0

with open("score.json", "r") as file:
    score_list=json.loads(file.read())
    score_list.sort()
    print(f"Top score: {score_list[:3]}")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        score_list.append(attempts)
        with open( "score.json", "w") as file:
            score_list.sort()
            file.write(json.dumps(score_list))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")