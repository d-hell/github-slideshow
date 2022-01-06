import random





going = True
while going:
	user_action = input("Enter your choice (Rock, Paper, Scissors):")
	possible_action = ["Rock", "Paper", "Scissors"]
	computer_action = random.choice(possible_action)

	print(f"/n You chose {user_action}, computer chose {computer_action}")
	if user_action == computer_action:
		print(f"Both Players selected {user_action}. It's a Tie!")

	elif user_action == "Rock":
		if computer_action == "Scissors":
			print("Rock smashes scissors! You win!")
		else:
			print ("Paper covers Rock. You lose!")

	elif user_action == "Paper":
		if computer_action == "Rock":
			print ("Paper covers Rock. You win!")
		else:
			print ("Scissors cuts Paper. You Lose!")

	elif user_action == "Scissors":
		if computer_action == "Paper":
			print ("Scissors cuts Paper. You Win!")
		else:
			print ("Rock smashes Scissors. You Lose!")

	another = input("Would you like to play again? [y/n]: ")
	if another == 'n':
		going = False
