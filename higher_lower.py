from game_data import data
from art import logo
from art import vs
import random

print(logo)

playing_game = True
score = 0
pick1 = random.choice(data)
pick2 = random.choice(data)

while playing_game:
    print(f"Compare A: {pick1['name']}, {pick1['description']} from {pick1['country']}.")
    print(vs)
    print(f"Your score is {score}.")
    print(f"Against B: {pick2['name']}, {pick2['description']} from {pick2['country']}.")
    a_or_b = input("Who has more followers on Instagram? Type 'a' or 'b': ").lower()
    if 'a' in a_or_b and pick1['follower_count'] > pick2['follower_count']:
        print("Correct!")
        print(f"{pick1['name']} has {pick1['follower_count']} million followers on Instagram.")
        print(f"while {pick2['name']} has {pick2['follower_count']} million followers on Instagram.")
        score += 1
        pick1 = pick2
        pick2 = random.choice(data)
        continue
    elif 'b' in a_or_b and pick2['follower_count'] > pick1['follower_count']:
        print("Correct!")
        print(f"{pick1['name']} has {pick1['follower_count']} million followers on Instagram")
        print(f"while {pick2['name']} has {pick2['follower_count']} million followers on Instagram.")
        score += 1
        pick1 = pick2
        pick2 = random.choice(data)
        continue
    else:
        print(f"Incorrect. You lose. Your score is {score}.")
        playing_game = False
    playing_game = False
