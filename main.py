import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#paper beats rock.
#scissors beats paper.
#rock beats scissors.

#Put game in a list and store in a variable.(list has a order that should be followed 0, 1, 2).
rps = [rock, paper, scissors]
#Give the user input and change it from str to int, cause you're dealing with whole numbers.
user = int(input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user >= 3 or user <0 :
  print ("Invalid number, you lose!")
else:
  print(rps[user])
  #Put computer in random and put it in a variable
  computer = random.randint(0, 2)
  #Print the variable computer.
  print ("Computer chose:")
  print(rps[computer])
  
  #if statements.
  
  if user == 0 and computer == 2 :
    print ("You win!")
  elif computer == 0 and user == 2 :
    print ("You lose!")
  elif computer > user :
    print ("You lose!")
  elif user > computer :
    print ("You win!")
  elif computer == user :
    print ("Draw")  