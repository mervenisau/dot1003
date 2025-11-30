#task54
print("The quick brown fox jumps over the lazy dog")
sentence="The quick brown fox jumps over the lazy dog"
question=input("Which item do tou want to search? ")
n=sentence.count(question)
print(f"item {question} appeared {n} times")
print("")
#task55
def ask():
    return(f"item {item} appeared {n} times")
search=input("Enter the input to search: ")
item=input("Which item do you want to search?: ")
n=search.count(item)
print(ask())
print("")
#task56

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
tersi = anarya(game_list)
print(tersi)   
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

