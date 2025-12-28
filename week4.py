#task40
repetition=int(input("How many repetiton for 'li': "))
city=input("Which word: ")
print(city + "li"*repetition + "lerle")
print("")
#task41
def compare(first, second):
    if len(first)>len(second):
        return first
    elif len(first)<len(second):
        return second
    else:
        return "Their length are same."
first_input= input("First Word: ")
second_input=input("Second Word: ")
print(compare(first_input, second_input))
print("")
#task42
a=str(input("Your input: "))
print(f"*{a}*")
print("")
#task43
a=str(input("Your input: "))
print(a)
print("-"* len(a))
print("")
#task44
text = input("Your Input: ")
total_width = 18       
inner_width = total_width - 2   
text_len = len(text)

if text_len > inner_width:
    text = text[:inner_width]
    text_len = inner_width
empty_space = inner_width - text_len
left_count = empty_space // 2         
right_count = empty_space - left_count 

top_bottom = "-" * total_width
middle = "|" + (">" * left_count) + text + ("<" * right_count) + "|"

print(top_bottom)
print(middle)
print(top_bottom)
print("")
#task45
a=str(input("Please enter string: "))
b=int(input("Please enter first integer: "))
c=int(input("Please enter last integer: "))
print(a[b:c])
print("")
#task46
a=str(input("Please enter string: "))
b=int(input("Please enter integer: "))
print(a[0:b])
print("")
#task47
a=str(input("Please enter string: "))
b=int(input("Please enter integer: "))
print(a[b:])
print("")
#task48
x=str(input("Please enter string: "))
print("found" if "a" in x else "not found")
print("")
#task49
x=str(input("Please enter string: "))
y=str(input("Please enter search item: "))
print("found" if y in x else "not found")
print("")
#task50
x=str(input("Please enter string: "))
y=str(input("Please enter search item: "))
a=x.find(y)
if a==-1:
       print("not found")
else:
       print(f"found it at {a}")
print("")
#task51
x="The quick brown fox jumps over the lazy dog"
q=str(input("What are you looking for? "))
while q!="-1":
       y=x.find(q)
       if y==-1:
             print("not found")
       else:
             print(f"Found it at {y}")
       q=str(input("What are you looking for? "))
print("Bye")
print("")
#task52
def to_two_decimal(num_list):
    new_list = []
    for n in num_list:
        new_list.append("{:.2f}".format(n))
    return new_list
my_list = [1.2345, 2.3456, 3.4567, 4.5678]
new_list = to_two_decimal(my_list)
print(new_list)
#Merve Nisa Ülger
#task 41 44 ve 52'de yapay zekadan yardım aldım
