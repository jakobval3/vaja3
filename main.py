import random
import json
import datetime


secret = random.randint(1, 30)
print(secret)
attempts = 0

player= input("who is playing? ")

with open("score.json", "r") as file:
    score_list=json.loads(file.read())
    for score_dict in score_list:
        print(f"{score_dict['attempts']} attempts, by {score_dict['player']} on {score_dict['date']}")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        score_list.append({"attempts": attempts,"player": player, "date": str(datetime.datetime.now())})
        with open( "score.json", "w") as file:

            file.write(json.dumps(score_list))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")