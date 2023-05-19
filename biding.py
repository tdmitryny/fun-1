from art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)
score = 0
random_b = random.choice(data)

game_should_continue = True

while game_should_continue:

  def format(account):
    random_name = account['name']
    random_dec = account['description']
    random_country = account['country']
    return f"{random_name}, a {random_dec}, {random_country}"

  def check_answer(guess, follower_a, follower_b):
    if follower_a > follower_b:
      return guess == "a"
    else:
      return guess == "b"

  #Generate random user
  random_a = random_b
  random_b = random.choice(data)
  
  #If they are same I need to make sure it regenrated
  if random_a == random_b:
    random_b = random.choice(data)

  #Format account in printable line
  print("Compare A: " + format(random_a))
  print(vs)
  print("Against B: " + format(random_b))

  #Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  #Get follower count of each account
  foll_a = random_a['follower_count']
  foll_b = random_b['follower_count']

  is_correct = check_answer(guess, foll_a, foll_b)
  clear()
  #Give uset feedback on guess
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    game_should_continue = False
    print(f"Sorry,you are wrong. Your final {score} ")


