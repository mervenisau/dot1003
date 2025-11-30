#task21
def x():
    print(f"Hello {a}")

a=input("Please input an argument: ")
x()
print("")
#task22
def x(a):
    return(f"Hello {a}")

y=input("Please input an argument: ")
print(x(y))
print("")
#task23
def sum(a,b):
 return a+b
print(sum(3,2))
print("")
#task24
def x(a):
   print(f"Hi {a}")
x("Andrew Ryan")
x("Gordon Freeman")
print("")
#task25
def mean(a,b,c):
   return (a+b+c)/3
print(mean(3,2,1))
print("")
#task26
a=input("Say my name: ")
while a!="Heisenberg":
 a=input("Say my name: ")
 print("You're goddamn right!")
print("")
#task27
a=input("Enter your name: ")
b=input("Enter again: ")
while a!=b:
 print("They are not same.")
 b=input("Enter again: ")
print("Your password matches and acount created successfully")
print("")
#task28
a=int(input("Please enter a number: "))
while a!=0:
 print(a)
 a=a-1
 if a==0:
  print("Kaboom")
print("")
#task29
attempts_left=3
flag=False
while attempts_left>0 and not flag:
    a=input("Password: ")
    if a==password:
        print("Welcome")
        flag=True
    else:
        attempts_left-=1
        if attempts_left>0:
            print("Try Again")
if not flag:
    print("Incorrect Password.Exterminate...")
print("")
#task30
print("dumb calculator v0.1 If you want to exit, enter 0")
sayı=0
toplam=0
tek=0
çift=0
n=int
n=int(input("please enter a number: "))
while n!=0:
    sayı+=1
    toplam+=n
    if n%2==0:
        çift+=1
    else:
        tek+1
    n=int(input("please enter a number: "))
print(f"Toplam sayı: {sayı}")
print(f"Sum: {toplam}")
if sayı>0:
    ortalama=toplam/sayı
    print(f"ortalama: {ortalama}")
else:
    print("Ortalama: N/A ")
print(f"tek: {tek} çift: {çift}")
print("")
#task31
x=[]
x.append(4)
x.append(5)
x.append(6)
print(x)
print(f"My first item is {x[0]}")
print(f"List lenght is {len(x)}")
x.pop(1)
print(x)
#task32
x=[]
x.append(7)
x.append(8)
x.append(9)
print(x)
x[0]=100
print(x)
print("")
#task33
x=[]
a=input("Please enter an input: ")
while a!="exit":
    x.append(a)
    a=input("Please enter an input: ")
    if a=="exit":
        print(x)
#task34
for i in x:
   print(i)
print("")
#task35
x=str(input("Please enter an input: "))
for i in x:
    print(i)
print("")
#task36
raw_points=[1,2,1,3]
total=0
for i in raw_points:
    total+=i
print(f"total {total} points earned")
print("")
#task37
raw_points=[1,-2,1,3,-5,7,0]
total=0
for i in raw_points:
   if i>0:
      total+=i
print(f"total {total} points earned")
print("")
#task38
n=int(input("Please input table size: "))
row="|" + "_|" * n
for _ in range(n):
    print(row)
print("")
#task39
height = int(input("Spruce height: "))
print() 
for i in range(height):
    spaces = height - i - 1      
    stars = 2 * i + 1            
    print(" " * spaces + "*" * stars)
print(" " * (height - 1) + "*")
#Merve Nisa Ülger
