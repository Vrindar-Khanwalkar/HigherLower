import random
import posix
from data import data
import art


def choose_question(dict_list):
  """
    This function chooses a random question from the list of questions.
    """
  return random.choice(dict_list)


#Chris Brown, a Musician, from United States.
def readable_followers(list):
  print(list['name'] + ', ' + list['description'] + ', ' + 'from ' +
        list['country'])


def compare_list(guess, follower1, follower2):
  if follower1 > follower2:
    return guess == 'a'
  else:
    return guess == 'b'


def game():
  print(art.logo)
  score = 0
  game_should_continue = True
  compareA = choose_question(data)
  compareB = choose_question(data)
  while game_should_continue:
    compareA = compareB
    compareB = choose_question(data)
    while compareA == compareB:
      compareB = choose_question(data)
      readable_followers(compareA)
      print(art.vs)
      readable_followers(compareB)
      follower1 = compareA['follower_count']
      follower2 = compareB['follower_count']
      guess = input("Which has more followers? Type 'A' or 'B': ").lower()
      is_correct = compare_list(guess, follower1, follower2)
      posix.system('clear')
      print(art.logo)
      if is_correct:
        score += 1
        print(f"You are right! Current score: {score}.")
      else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")


game()
