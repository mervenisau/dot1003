#task67
def coordinator(x,y):
    my_tuple=(x,y)
    return my_tuple

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
my_coordinates = coordinator(a,b)
print(my_coordinates)
print("")
#task68
def coordinator(x,y):
    return (x,y)

my_coordinates={}
my_coordinates[coordinator(0,0)]="Home"
my_coordinates[coordinator(1,1)]="Work"
my_coordinates[coordinator(-1,-1)]="School"

for k,v in my_coordinates.items():
    print(f"position: {k}, name: {my_coordinates[k]}")
print("")
#task69
def print_best_weapon(weapon_list):
    best = weapon_list[0] 
    for weapon in weapon_list:
        if weapon[1] > best[1]: 
            best = weapon
    print(best[0])   
weapon1 = ("blade", 10)
weapon2 = ("sabre", 35)
weapon3 = ("sword", 50)

meele_weapon = [weapon1, weapon2, weapon3]
print_best_weapon(meele_weapon)
#task70
def coordinator(x, y):
    return (x, y)
def print_board(board):
    for row in board:
        print(" ".join(row))
EMPTY = "_"
game_table = [[EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]
user_inputs = []
print_board(game_table)
flag = True
while flag:
    command = input("please type new or exit: ")
    if command == "exit":
        flag = False
    elif command == "new":
        x = int(input("please enter x: "))
        y = int(input("please enter y: "))
        if 0 <= x <= 2 and 0 <= y <= 2:
            user_inputs.append(coordinator(x, y))
        else:
            print("Invalid coordinate (use 0,1,2).")

for (x, y) in user_inputs:
    game_table[y][x] = "*" 

print_board(game_table)
print("")
#task71
my_set=set()
your_element=input("Enter an element for set: ")
while your_element!="exit":
    my_set.add(your_element)
    your_element=input("Enter an element for set: ")
for item in my_set:
    print(item)
print("")
#task72
my_set=set()
your_element=input("Enter an element for set: ")
while your_element!="exit":
    if your_element in my_set:
        print(f"{your_element} is already in our set.")
    else:
        my_set.add(your_element)
        your_element=input("Enter an element for set: ")
for item in my_set:
    print(item)
print("")
#task74
print("Local variables: my_ans")
print("Global variables: real_age, name, question, user_guess")
print("")
#task75
def start_game():
    global score
    score = 10
    print(f"Game started! Current score: {score}")

def increase_score():
    global score
    score += 5
    print(f"Score increased! Current score: {score}")

def display_score():
    print(f"Final score: {score}")

score = 0
start_game()
increase_score()
display_score()
print("")
#task76
def age_calc():
    current_year = 2026
    my_flag = False
    while not my_flag:
        try:
            birthyear = int(input("What is your birthyear? "))
            my_flag = True
        except ValueError:
            print("Invalid Input.")
    return current_year - birthyear
print(f"You are {age_calc()} years old")
print("")
#task77
print("Bu kod SyntaxError verir. Çünkü genel expect en üstte olamaz")
x = int(input("Please enter a number: "))
my_flag = True
while my_flag:
    try:
        y = int(input("Please enter divider: "))
        print(f"{x} divided by {y} is {x / y}")
        my_flag = False
    except ZeroDivisionError:
        print("You can’t enter 0 as divider")
    except ValueError:
        print("Invalid Value")
    except:
        print("Some kind of error occured")
print("")
#task78
def new_game():
    name = input("game name: ")
    if name == "":
        raise ValueError("Name cannot be empty.")
    if len(name) > 40:
        raise ValueError("Name cannot be longer than 40 characters.")

    try:
        year = int(input("release year: "))
    except ValueError:
        raise ValueError("Release year must be an integer.")

    if year < 0:
        raise ValueError("Release year cannot be negative.")
    if year > 2024:
        raise ValueError("Release year cannot be greater than 2024.")

    return (name, year)
game_list = []
flag = True
while flag:
    user_command = input("add or exit: ")
    if user_command == "exit":
        flag = False
    elif user_command == "add":
        try:
            game_list.append(new_game())
        except ValueError as e:
            print(e)
for game in game_list:
    print(f"Name: {game[0]}, Year: {game[1]}")
print("")
#task79
def factorial(n):
    if n < 0:
        raise ValueError("No negative value")
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k
try:
    print(factorial(5))
except ValueError as e:
    print(e)
try:
    print(factorial(-1))
except ValueError as e: