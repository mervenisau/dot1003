#task54
print("The quick brown fox jumps over the lazy dog")
sentence="The quick brown fox jumps over the lazy dog"
question=input("Which item do tou want to search? ")
n=sentence.count(question)
print(f"item {question} appeared {n} times")
print("")
#task55
def question(search1,item1):
    n=search1.count(item1)
    return (f"item {item1} appeared {n} times")
a=input("Enter the input to search: ")
b=input("Which item do you wan to search?: ")
print(question(a,b))
print("")
#task56
def clear_vowels(text):
    vowels="aeiouAEIOU"
    new_text=""

    for x in text:
        if x not in vowels:
            new_text+=x
    return new_text

menu_button=input("Enter a text: ")
print(clear_vowels(menu_button))
print("")
#task57
def anarya(game_list):
    game_list.reverse()
    return game_list

game_list = []
game = input("Enter a game: ")

while game != "exit":
    game_list.append(game)
    game = input("Enter a game: ")

print(game_list)               
print(anarya(game_list))
print("")
#task58
def anarya(game_list):
    reversed_list = []

    i = len(game_list) - 1     
    while i >= 0:
        reversed_list.append(game_list[i])
        i = i - 1            
    return reversed_list

game_list = []
game = input("Enter a game: ")

while game != "exit":
    game_list.append(game)
    game=input("Enter a game: ")

print(game_list)
tersi=anarya(game_list)
print(tersi)
print("")
#task59
def shortest_name(game_list):
    shortest = game_list[0]
    i = 1
    while i < len(game_list):
        if len(game_list[i]) < len(shortest):
            shortest = game_list[i]
        i = i + 1
    return shortest

game_list = []
game = input("Enter a game: ")

while game != "exit":
    game_list.append(game)
    game = input("Enter a game: ")

print("Game list:", game_list)

if len(game_list) == 0:
    print("You didn't enter any game.")
else:
    shortest = shortest_name(game_list)
    print("Shortest name:", shortest)
print("")
#task60
def finder(matrix, element):
    i = 0
    while i < len(matrix):              
        j = 0
        while j < len(matrix[i]):       
            if matrix[i][j] == element:
                print("find at row:", i, "column:", j)
                return True
            j = j + 1
        i = i + 1
    return False


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
element = int(input("item to search: "))

i = 0
while i < len(my_matrix):
    print(my_matrix[i])
    i = i + 1
print(finder(my_matrix, element))
print("")
#task61
def sum_of_row(matrix, row_no):
    row = matrix[row_no]   # istenen satır
    total = 0
    j = 0
    while j < len(row):
        total = total + row[j]
        j = j + 1
    return total

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

i = 0
while i < len(my_matrix):
    print(my_matrix[i])
    i = i + 1

row_no = int(input("Which row do you want to sum (0-2): "))
print("Sum of row", row_no, "is", sum_of_row(my_matrix, row_no))
print("")
#task63
def tripler(numbers):
    new_list = []
    for n in numbers:
        new_list.append(n * 3)
    return new_list

my_lucky_numbers = [4, 8, 15, 16, 23, 42]
tripled_numbers = tripler(my_lucky_numbers)

print(f"My Lucky Numbers: {my_lucky_numbers}")
print(f"Tripled Numbers: {tripled_numbers}")
print("")
#task64
inventory = {
    "item1": 3,
    "item2": 1,
    "item3": 5
}

for key, value in inventory.items():
    print(f"{key}: {value}")
print("")
#task65
inventory = {
    "item1": 3,
    "item2": 1,
    "item3": 5
}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

add_item("item1", 5)
add_item("item4", 1)

for key, value in inventory.items():
    print(f"{key}: {value}")
print("")
#task66
inventory = {"item1": 3, "item2": 1, "item3": 5}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def remove_item(item, quantity):
    if item not in inventory:
        return  # item yoksa çık

    new_qty = inventory[item] - quantity

    if new_qty < 0:
        new_qty = 0

    if new_qty == 0:
        del inventory[item]      # Task 66: 0 olunca sil
    else:
        inventory[item] = new_qty

# Test (PDF’deki örneğe benzer)
add_item("item1", 5)
add_item("item4", 1)

remove_item("item4", 6)
remove_item("item1", 2)

for key, value in inventory.items():
    print(f"{key}: {value}")
print("")

#task56 ,64.65 ve 66 için yapay zekadan yardım aldım