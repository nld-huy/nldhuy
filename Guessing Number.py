from random import randint
Number = randint(1, 100)

#Hint1: Showing the number id odd or even
if Number % 2 == 0: 
    print("Hint 1: It is even")
elif Number % 2 != 0:
    print("Hint 1: It is odd")
	
#Hint2: Showing the range to narrow 
if Number < 25:
    print("Hint 2: Number <= 25")   
elif Number < 50:
    print("Hint 2: 25 <= Number <= 50")
elif Number < 75:
    print("Hint 2: 50 <= Number <= 75")
elif Number >= 75:
    print("Hint 2: Number >= 75")
	
#Hint3: Showing if this number can devide for 3,5,7,10
hint3 = [3,5,7,10]
chuoi_hint3 = []
check_hint3 = 0 
for i in hint3:
    if Number % i == 0:
        chuoi_hint3.append(i)
        check_hint3 += 1
if check_hint3 == 0:
    print("Hint 3: It is not divisible by 3,5,7,10")
if check_hint3 > 0:
    print("Hint 3: It is divisible by",chuoi_hint3)
	
#Hint4: Showing if this number is prime or not
check_hint4 = True  	#check_hint4 is a checking variable
if (Number < 2):
    check_hint4 = False
elif (Number == 2):
    check_hint4 = True
elif (Number % 2 == 0):
    check_hint4 = False
else:
    #Looping through odd numbers should start at 3 with a jump of 2
    for i in range(3, Number, 2):
        if (Number % i == 0):
            check_hint4 = False
if check_hint4 == True:
    print("Hint 4: This is a prime number")
else:
    print("Hint 4: This is not a prime number")
	
#Hint 5: Showing the number tens of this number
print("Hint 5: The tens number of this number is",int(Number/10))

#After receive 5 hints, Player will guess the number
print("-------------")
Player = int(input("So this number is: "))
print("-------------")
if Player == Number:
    print("Correct. Are you a mind-reader?")
else:
    print("Wrong. See you next time, Stupid")