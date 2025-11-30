#task11
x=int(input("Please type in a temperature (F): "))     
y=(x-32)*5/9
print(f"{x} degrees  Fahrenheit equals {y} degrees Celcius ")
if y<0:
 print("Brr! It's cold in here!")
print("")
#task12
x=float(input("Hourly wage: "))
y=int(input("Hours worked: "))
z=input("Day of the week: ")

if z=="Sunday":
 print(f"Daily wages: {x*y*2} liras ")
else:
 print(f"Daily wages: {x*y}") 
print("")
#task13
x=int(input("How old are you? "))
if x<18:
 print("You can't play Dark Souls")
elif x<43:
 print("Here is Dark Souls. Lol")
else:
 print("YoU are too old for this shit")
print("")
#task14
x=float(input("Type the first number: "))
y=float(input("Type the second one: "))
if x>y:
 print(f"First one is greater {x}>{y}")
elif x<y:
 print(f"Second one is greater {x}<{y}")
else: 
 print(f"These are equal {x}={y}")
print("")
#task15
x=input("Type the first word: ")
y=input("Type the second one: ")
if x>y:
 print(f"{x} comes alphabetically last")
elif x<y:
 print(f"{y} comes alphabetically last")
else:
 print("These are same!")
print("")
#task16
x=input("Which community do you belong to?: ")
if x== "New California" and "Brotherhood of Steel" and " Ceaser's Legion" and "Great Khans" and "Vault Dweller":
 print("You're belong to Fallout Universe")
else:
 print("Nope, You are not belong to Fallout Lore ")
print("")
#task17
x=int(input("How many point [0-100]: "))
if x>100:
 print("impossible!")
elif x>=90:
 print("5")
elif x>=80:
 print("4")
elif x>=70: 
 print("3")
elif x>=60:
 print("2")
elif x>=50:
 print("1")
elif x>=0:
 print("fail")
else:
 print("You what?")
print("")
#task18
x=int(input("Enter number: "))
if x%15==0:
 print("FizzBuzz")
elif x%5==0: 
 print("Buzz")
elif x%3==0:
 print("Fizz")
print("")
#task19
x=int(input("Please type in a number: "))
if x>0 and x%2==0:
 print("The number is even")
elif x>0 and x%2==1:
 print("The number is odd")
else:
 print("The number is negative or zero")
print("")
#task20
x=int(input("Please type in a year: "))
if x%400==0:
 print("That year is a leap year.")
elif x%100==0:
 print("That is not a leap year.")
elif x%4==0:
 print("That is a leap year")
else:
 print("That year is not a leap year.")
 #Merve Nisa Ülger