##########################################################
## THE HORROR DUNGEON - My first ever py game **Drum roll**
##########################################################

title = "The horror dungeon: where every choice you make matters"
print(title)

""""
META DATA starts
""""
import time
import random

#As the user progresses in the game and performs actions to acquire tools, the values in the tools dictionary are updated accordingly.
tools = {
	"match_sticks": False,
	"spinach": False,
	"aerosol_spray": False,
	"pills": False,
	"poison": False,
	"gun": False
}

#After updating tools, they are added to backup to display tools the user has.
backpack = []

#Health Indicator. use % here to display health
health = 100

#Money
coins = 100

#Storing the answers
true = ["T", "t", "True", "true"]
false = ["F", "f", "False", "false"]
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Directing user to choose valid response
required = ("\nChoose a valid option\n")

print("Welcome to the horror dungeon where YOUR choice matters.\nYou find yourself in a mysterious and captivating game created by an enigmatic creator. The rules are simple yet challenging - you must navigate through a series of five rooms, each filled with its own unique set of puzzles, riddles, and tests. Your ultimate objective is to escape this perplexing labyrinth and claim your freedom. Armed with your wits and a trusty backpack, you scavenge for supplies, searching dark rooms in an abandoned building. Your backpack holds the key to your survival, containing tools and weapons that can help you fend off the relentless danger. But beware, not all tools are effective against the undead. You must choose wisely and strategize your every move. Each decision you make will impact your chances of survival. The creator has set the stage, but it is up to you to determine your destiny.\n\n")
#time.sleep(10)

#Current stat for each round
def current_stat(): # Using user_name placeholder here which is called after getting the user name.
	print(f"Player {user_name.title()}, \nYour health is at {health}%. \nYou have {coins} coins.")
	if len(backpack) == 0:
		print("0 items in your backpack. Collect some items.\n")
	else:
		print("\nCurrently you have these objects in your backpack:\n")
		for item in backpack:
			print(f"- {item.title()}")

# Information greetings
GreetIntro = "As you enter the first room, the heavy door slams shut behind you, trapping you inside. You see two undead characters. You are intrigued but scared at the same time. Will they hurt you or help you get through this trecherous game, only time will tell."

GreetQuiz = "To find the key and unlock the next room, you must solve intricate riddles, unravel hidden clues, and demonstrate your wisdom. With each wrong choice you make, your health depletes. \nAnswer atleast 4 questions correctly & if you don't you die. If you happen to be a genius and answer all questions correctly, I'll let you skip all rooms and give you a 'chance' at final room"

GreetDragon = "In the Dragon Room, you find yourself in a chamber engulfed in an eerie silence, broken only by the distant sound of heavy breathing. As your eyes adjust to the dim light, you see an enormous dragon, its scales glistening ominously under a single flickering torch.\nYour heart pounds in your chest as the dragon's fiery gaze fixes upon you. Its eyes, burning with an insatiable hunger, convey a deadly challenge."

GreetZombie = "As you step into this room, you are surrounded by the dead. Only those who persevere will be granted passage to the final room. A zombie is approaching you."

GreetChance = "In the last room, you face the ultimate trial - a confrontation with your luck. There's nothing much you can do except praying that God doesn't choose this day as a doomsday for all your sins. To overcome this final hurdle and escape the game, you must confront the creator, make peace with the result, and find the courage to pull that trigger...."
"""
META DATA ends
"""

user_name = input("Enter your name: ")
print("")
# Room 1: The Room of Introduction
def intro():
	current_stat()
	time.sleep(3)
	print(f"{GreetIntro} \n\nYou will:")
	time.sleep(7)
	print("\tA. Talk to the mystic man\n\tB. Talk to the old turtle\n\tC. Move on to the next round")
	choice = input("Type A/B/C : ")  # User's first choice.
	if choice in answer_A:
		mystic_man()
	elif choice in answer_B:
		old_turtle()
	elif choice in answer_C:
		game_quiz()
	else:
		print(required)
	intro()


# Character 1
def mystic_man():
	print("\nYou are a brave soul that you entered here. Don't trust anyone since it's a game of grandeur. I can help you pass through if you may surrender. Do you pick up the poison?")
	choice = input("Y/N : ")
	if choice in yes:
		print("Rest in peace now...")  # adds a poison
		quit()
	elif choice in no:
		print("You are clever")
		tools["aerosol_spray"] = True  # unlock an aerosol
		print("\n'You acquired an aerosol'")
		backpack.append("aerosol spray")
		time.sleep(1)
		print("New tool added to the backpack..")
		time.sleep(3)
		mystic_man_conversation()
	else:
		print("Please enter a valid choice.")
		mystic_man()


#Conversation logic with mystic man where user can unlock more tools or get useful information
def mystic_man_conversation():
	print("\nI really wanna help you this time. Which one would you pick:")
	time.sleep(1)
	print ("\tA. An advice\n\tB. A gun\n\tC. Leave the conversation")
	choice = input("Type A/B/C : ")
	if choice in answer_A:
		print("\n\nBe safe out there.\n\n")
		time.sleep(2)
		intro()
	elif choice in answer_B:
		tools["gun"] = True  # unlock a gun
		print("\n'You acquired a gun'")
		backpack.append("gun")
		time.sleep(1)
		print("New tool added to the backpack..")
		time.sleep(3)
		intro()
	elif choice in answer_C:
		intro()
	else:
		print (required)

# Character 2
def old_turtle():
	print("\nOld Turtle : 'A treasure that you can see is not a treasure. Keep your mind open to the possibilities and you may live long' "
"\nOld turtle gives you a match stick. Do you take it? ")
	choice = input("Y/N : ")
	if choice in yes:
		tools["match_sticks"] = True  #Adds a stick
		print("\n'You acquired a match stick'")
		backpack.append("match stick")
		time.sleep(1)
		print("New tool added to the backpack..")
		time.sleep(3)
		intro()
	else:
		print("I offered a useful tool, you 'tool'\n")
		time.sleep(2)
		old_turtle_conversation()

		#Conversation logic with old turtle and some unlock tools or useful information
def old_turtle_conversation():
	print("You seem to have some doubts. I shall grant you one of these or all of these if you keep returning back to piss me off")
	print("\tA. Get a golden advice\n\tB. Get some Spinach and Pills \n\tC. Solve an equation to proceed directly to the 4th round")
	choice = input("Type A/B/C : ")
	if choice in answer_A:
		print("\n'To kill a breath stinker you might or might not meet later, use some combination of items that sprays fire.'")
		time.sleep(3)
		intro()
	elif choice in answer_B:
		tools["spinach"] = True  #Adds spinach
		print("\n'You acquired Spinach'")
		backpack.append("spinach")
		time.sleep(1)
		print("New tool added to the backpack..")
		time.sleep(3)
		tools["pills"] = True  #Adds pills
		print("\n'You acquired Pills'")
		backpack.append("pills")
		time.sleep(1)
		print("New tool added to the backpack..")
		time.sleep(3)
		intro()
	elif choice in answer_C:
		print("Great! Hopefully you are a math genius because more than 50% of students at Harvard, MIT, and Princeton got this question wrong.")
		time.sleep(1)
		print("\n\nA bat and ball cost $1.10.\nThe bat costs one dollar more than the ball. \nHow much does the ball cost?")
		choice = input("Your Answer : ")
		if choice in ["5 cents", "five cents", "five cent", "5 cent"]:
			print("YOU REALLY ARE A GENIUS.\nyou move to the 4th round....")
			time.sleep(3)
			game_zombie()

######

#Room 2: The Room of Quiz

def game_quiz():
	print("")
	current_stat()
	time.sleep(3)
	print(f"{GreetQuiz} \n\n")
	time.sleep(7)
	correct = 0 # Initialised the correct variable
	global health  # Declare 'health' as a global variable to modify it within the function

	print("*" * 50 +
"\n" +
"*" + " " * 48 + "*" +
"\n" +
"*" + " Time for some riddles ".center(48) + "*" +
"\n" +
"*" + " " * 48 + "*" +
"\n" +
"*" * 50)

	time.sleep(2)

	print ("\nI touch the earth and I touch the sky, but if I touch you, you’ll likely die. What am I?")
	choice = input("\nOne word response: ")
	if choice.lower() == "lightning":
		correct += 1
	else:
		health -= 20  #reduced redundancy by omitting correct +=0 instead penalised for incorrect response by reducing health
	print("Health:", health)  #Display the updated health value


	time.sleep(1)

	print ("\nI follow you wherever you go, but I never have a presence. What am I?")
	choice = input("One word response: ")
	if choice.lower() == "shadow":
		correct += 1
	else:
		health -= 20
	print("Health:", health)

	time.sleep(1)

	print ("\nWho is the better actor: Tom Cruise or Tom Brady?")
	choice = input("Choose one: ")
	if choice.lower() == "tom cruise":
		correct += 1
		print("You're right, Tom Cruise is the one")
	else:
		print("Oops, I don't think so")
		health -= 20
		print("Health:", health)

	time.sleep(1)
	print("")

	print("*" * 50 +
"\n" +
"*" + " " * 48 + "*" +
"\n" +
"*" + " Let's test your geography ".center(48) + "*" +
"\n" +
"*" + " " * 48 + "*" +
"\n" +
"*" * 50)

	print ("\nWhat is the world’s smallest country?")
	choice = input("\nResponse: ")
	if choice.lower() == "vatican city":
		correct += 1
	else:
		health -= 25
		print("Health:", health)

	print ("\nWhat is the most populous city in the world?")
	choice = input("\nResponse: ")
	if choice.lower() == "tokyo":
		correct += 1
	else:
		health -= 25
		print("Health:", health)
	time.sleep(1)
	print("")

	print("*" * 50 +
"\n" +
"*" + " " * 48 + "*" +
"\n" +
"*" + " Let's see if you passed high school or not ".center(48) + "*" +
"\n" +
"*" + " " * 48 + "*" +
"\n" +
"*" * 50)

	print ("\nTrue or False: The Great Wall of China is visible from space.")
	choice = input("T/F : ")
	if choice in false:
		correct += 1
	else:
		health -= 30
		print("Health:", health)

	print ("\nTrue or False: The sum of all the angles in a triangle is always 180 degrees.")
	choice = input("T/F : ")
	if choice in true:
		correct += 1
	else:
		health -= 30
		print("Health:", health)

	print(f"Your total score is {correct}.")
	print("")
	time.sleep(2)

#First check if a perfect score=7, then send user directly to last round, and if score is atleast 4, user passes to next round otherwise, user fails and game breaks.
	if correct == 7:
		print("Congratulations! You answered all questions correctly")
		time.sleep(3)
		print("Proceeds to the last round....")
		game_chance()

	elif correct >= 4:
		print("Congratulations! You answered atleast 4 questions correctly")
		time.sleep(3)
		print("Proceeds to the next round....")
		game_dragon()	
	else:
		print("You died...")
		exit()

#################

# Room 3: The Room of Dragons
print("""""")
def game_dragon():
	current_stat()
	time.sleep(3)
	print(f"{GreetDragon} \n\nYou encounter a fearsome dragon! What do you do?")
	time.sleep(7)
	print("\tA. Run \n\tB. Hide \n\tC. Look in your backpack")
	choice = input("Type A/B/C : ")
	if choice in ['A', 'a']:
		option_run()
	elif choice in ['B', 'b']:
		option_hide()
	elif choice in ['C', 'c']:
		option_backpack1()
	else:
		print("Invalid choice. Try again.")
	game_dragon() # Recursive call to gane_dragon for restart

def option_run():
	print("\nYou try to run away, but the dragon's fiery breath catches up to you. You didn't make it.")
	print("Game Over!")

def option_hide():
	print("\nYou find a hiding spot, but the dragon's keen senses spot you. It unleashes its fury upon you.")
	print("Game Over!")

def option_backpack1():
	print("\nYou open your backpack and find the following tools:")
	for tool, available in tools.items():
		if available:
			print(f"- {tool}")
			print("What tool(s) do you want to use? (Separate multiple tools with commas)")
			choice = input("Type A/B/C : ")

			selected_tools = [tool.strip().lower() for tool in choice.split(",")]

# Check if all selected tools are available
			if all(tools.get(tool) for tool in selected_tools):
# Check for specific combinations
				if "matchstick" in selected_tools and "aerosol spray" in selected_tools:
					print("\nYou use the matchstick and aerosol spray combination. The dragon is engulfed in flames and collapses.")
					print("Congratulations! You defeated the dragon!")
				else:
					print("\nThat combination of tools is not effective against the dragon. It attacks you.")
					print("Game Over!")
		else:
			print("\nOne or more selected tools are not available or do not exist. Choose another option.")
		option_backpack1()

	game_zombie()

#################

# Room 4: The Room of Zombies
print("""""")
def game_zombie():
	current_stat()
	time.sleep(3)
	print(f"{GreetZombie} \n\nYou encounter a terrifying zombie! What do you do?")
	time.sleep(7)
	print("\tA. Run \n\tB. Hide \n\tC. Look in your backpack""")
	choice = input("Type A/B/C : ")
	if choice in ['A', 'a']:
		option_run()
	elif choice in ['B', 'b']:
		option_hide()
	elif choice in ['C', 'c']:
		option_backpack2()
	else:
		print("Invalid choice. Try again.")
	game_zombie()

def option_run2():
	print("\nYou try to run away, but the zombie chases you down and catches you. You didn't make it.")
	print("Game Over!")
	exit()

def option_hide2():
	print("\nYou find a hiding spot, but the zombie's keen senses detect you. It grabs you and bites you.")
	print("Game Over!")
	exit()

def option_backpack2():
	if not backpack:
		print("No tools in your backpack. Go back and grab some tools.")
		game_zombie()
	print("\nYou open your backpack and find the following tools:")
	for tool in backpack:
		print(f"- {tool}")

	print("What tool do you want to use?")
	choice = input("Select a tool : ")

# Check if selected tool is in the backpack list
	if choice in backpack:
		if choice == "gun":
			print("\nYou use the gun. The zombie takes multiple bullets in the head.")
			print("The zombie falls to the ground, defeated.")
			print("\nCongratulations! You survived the zombie encounter!")
			print("/n/nYou move on to the next and last round 'game of chance'.")
			game_chance()
			time.sleep(3)
		else:
			print("\nThat tool is not effective against the zombie. It attacks you.")
			print("Game Over!")
	else:
		print("\nThe selected tool is not available or does not exist. Choose another option.")

	option_backpack2()



##################

# Room 5: The Room of Chance
print("""""")
def game_chance():
	current_stat()
	time.sleep(3)
	print(f"{GreetChance} \n")
	print(f'Creator says "The world is a cruel place, and in this cruel world, the only notion of morality is left to chance. \nUnbiased, impartial, and fair. \nNow, let us determine your fate through a game of Russian roulette. \nWithin the barrel of this gun lie two bullets, and whoever the barrel favors shall taste the bittersweet embrace of death....muhahahahahah" *cough cough* \n\n')
	time.sleep(7)

	chambers = [0, 0, 1, 0, 0, 1]  #1 represents the bullet, 0 represents an empty chamber
	random.shuffle(chambers)  #Randomly shuffle the chambers

	while True:
		input(f"{user_name}, press Enter to pull the trigger...")
		outcome = chambers.pop()

		if outcome == 1:
			print("You may have been free, you loved loving your lie, fate had its own scheme, crushed like a bug you still die. Boom! \nYou're dead.")
			break
		else:
			print("\nPhew! The gun didn't fire. You survived!\n")

		input("Creator is pulling the trigger... Press Enter to continue...")
		outcome = chambers.pop()

		if outcome == 1:
			print("Ahhhh, you son of a gun. You may have survived this game. But I'll see you very soon!")
			print("\n\n\n CONGRATULATIONS!!!! YOU WON ".center(50,"*"))
			break
		else:
			print("\nPhew! The gun didn't fire. The computer survived!\n")

intro()
