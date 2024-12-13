#PRACTICLE 1
'''
#AIM  : Write a Python Program to accept username and password from user and display them.
#Name : Yash
#Date :

#Accepting username & Password from user
username = input("Enter your Username : ")
password = input("Enter your password : ")

#Displaying Username and Password
print("Username :",username,"\nPassword :",password)
'''
#========================================================================================================================
'''
#AIM  : Write a Python Program to accept principal amount, rate of interest and number of term years and display the simple interest using python. (Hint SI=P*N*R/100)
#Name : Yash
#Date :

#Getting user input for principal amount
principal_amount = float(input("Enter Principal amount : "))
#Getting user input for rate of interest
rate_of_interest = float(input("Enter Rate of interesr : "))
#Getting user input for no. of years
no_of_years = float(input("Enter no. of years : "))

#Calculating simple interest-of
simple_interest = (principal_amount*rate_of_interest*no_of_years)/100

#Displaying calculated Simple interest
print("Simple Interest : ",simple_interest)
'''
#========================================================================================================================
'''
#AIM  : Write a python program code to find the square of a number , cube of a number, square root and cube root of a number accepted from the user.
#Name : Yash
#Date :

#Accepting a number input form user
num = float(input("Entera number : "))

#Calculating square of number
square = num*num
#Displaying calculated square of number
print(f"Square of {int(num)} is {int(square)}")

#Calculating cube of number
cube = num**3
#Displaying calculated cube of number
print(f"cube of {int(num)} is {int(cube)}")

#Calculating square root of number
square_root = num**(1/2)
#Displaying calculated square root of number
print(f"Square root of {int(num)} is {square_root}")

#Calculating cube root of number
cube_root = num**(1/3)
#Displaying calculated cube root of number
print(f"cube root of {int(num)} is {cube_root}")
'''
#========================================================================================================================
'''
#AIM  : Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Name : Yash
#Date :

#Getting username from user
username = input("Enter your name : ")
#Getting user age input from user
user_age = int(input("Enter your age : "))

#Displaying user name and age
print(f"username : {username} \nAge : {user_age}")
#Current year
current_year = 2024

#Calculating year turn 100
year_turn_100 = current_year + (100 - user_age)

#Displaying the message
print(f"{username} you will turn 100 years old in year {year_turn_100}")
'''
#========================================================================================================================
'''
#AIM  : Python progrsm to calculate the gross salary of an employee for following allowance and deduction
#DATE :
#NAME : Yash

print("SALARY PROGRAM")

#Getting employee name
name = input("Enter name of employee : ")

#Getting Basic salary from employee
basic_salary = float(input("Enter the basic salary of the employee : "))

#Creating salary details slip
print("\nSALARY DETAILS")
print("=====================================================")
#Displaying employee name
print("Name of employee : ",name)

#Displaying employee basic salary
print("Basic salary of employee : ",basic_salary)

#Calculated Dearness Allow
dearness_allow = 25/100 * basic_salary
#Displaying Dearness Allow
print("DEARNESS ALLOW : ",dearness_allow)

#Calculated House Rent Allow
hour_rent_allow = 15/100 * basic_salary
#Displaying House Rent Allow
print("HOUSE RENT ALLOW : ",hour_rent_allow)

#Calculated Travel Allow
travel_allow = 7.50/100 * basic_salary
#Displaying Travel Allow
print("TRAVEL ALLOW : ",travel_allow)

print("======================================================")

#Calculated Net Pay
net_pay = basic_salary + dearness_allow + hour_rent_allow + travel_allow
#Displaying Net Pay
print("NET SALARY PAY : ",net_pay)

#Calculated Provident Fund
provident_fund = 12/100 * basic_salary
#Displaying Provident Fund 
print("PROVIDENT FUND : ",provident_fund)

#Calculated Tax
tax = 5/100 * basic_salary
#Displaying Tax
print("TAX : ",tax)

print("=====================================================")

#Calculated Gross Pay
gross_pay = net_pay - provident_fund - tax
#Displaying Gross Pay
print("GROSS PAYMENT : ",gross_pay)

print("=====================================================")
'''
#========================================================================================================================
#========================================================================================================================

#PRACTCLE 2
'''
#AIM  : Write a python program code to print triangle patterns using nested for loop.
#Name : Yash
#Date :

# Set the number of rows for the pattern
n = 5

# Loop through each row from 1 to n (inclusive)
for i in range(1, n + 1):
    # Print leading spaces to center the pyramid shape
    print("  " * (n - i), end=" ")

    # Print the increasing sequence of numbers for this row
    # The range starts at i and ends just before 2*i
    for j in range(i, 2 * i):
        print(j, end=" ")

    # Print the decreasing sequence of numbers for this row
    # The range starts at 2*i-2 and goes down to i (inclusive)
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end=" ")

    # Move to the next line after printing a row
    print()
'''
#========================================================================================================================
'''
#AIM  : Write a python program code to find Fibonacci of a number.
#Name : Yash
#Date :

#Accepting a number from user
num = int(input("Enter a number : "))
#Initialize the first two terms of the Fibonacci sequence
a,b = 0,1

print("Fibonacci Sequence")
# Loop 'num' times to generate and print the Fibonacci sequence
for i in range(num):
    #Print the current term (a) and stay on the same line
    print(a,end=" ")
    a,b = b,a+b
'''
#========================================================================================================================
'''
#AIM  : Write a python program code to find Armstrong of a number accepted from the user.
#Name : Yash
#Date :

#Accepting a number from user
num = int(input("Enter a number : "))
len_num = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while(temp>0):
    digit = temp%10
    sum += digit**len_num
    temp //= 10

# display the result
if sum == num:
    print(f"{num} is Armstrong number")
else:
    print(f"{num} is not an armstrong number")
'''
#========================================================================================================================
'''
#AIM  : Write a python program to reverse a number. Accept the number from the user.
#Name : Yash
#Date :

#Accepting nummber from user
num = int(input("Enter a number : "))

#Initializing Reverse number as 0
reverse_num = 0

while num!=0:
    digit = num%10
    reverse_num = reverse_num * 10 + digit
    num //= 10
print(f"Reverse number is {reverse_num}")
'''
#========================================================================================================================
'''
#AIM  : Write a python program to check whether username and password are correct for 3 times else lock the username.
#Name : Yash
#Date :

#Pre define username and password
username = "Obito"
password = "Rin"

attempt = 0
max_attempt = 3

while attempt<max_attempt:
    user = input("Enter your username : ")
    passwd = input("Enter your pasword : ")
    if user == username and passwd == password:
        print("Access Granted")
        break
    else:
        attempt += 1
        print("Invalid username or password!! \nTry Again")

if attempt == max_attempt:
    print("Your Account is Locked")
''' 
#========================================================================================================================
#========================================================================================================================

#PRACTICLE  3

'''
#AIM  : Write a program to implement a list in Python for suitableproblems. Demonstrate various operations on it.
#Name : Yash
#Date :

#Creating a list
blue_lock = ["Isagi","Bachira","Megumi","Chigiri"]
#Displaying list
print(f"List : {blue_lock}")

#Appending an element
blue_lock.append("Rin itoshi")
print(f"After appending 'Rin Itoshi' in list {blue_lock}")

#Inserting an element at a specific position
blue_lock.insert(2,"Gagamaru")
print(f"After inserting 'Gagamaru' at index 2 : {blue_lock}")

#Removing an element
blue_lock.remove("Megumi")
print(f"After removing 'Megumi' : {blue_lock}")

#Sorting list
blue_lock.sort()
print(f"After sorting list : {blue_lock}")

#Accessing an element
print(f"Accessing second name in list : {blue_lock[1]}")

#Length of list
print(f"Length of list : {len(blue_lock)}")
'''
#========================================================================================================================
'''
#AIM  : Create a flower list to store N elements accepted from the user in the list.
#Name : Yash
#Date :
    
#Creating an empty flower list
Flower_list = []

#Accepting the no of flower user wants
no_of_flower = int(input("Enter the no of flower you want : "))

for i in range(no_of_flower):
    flower_name = input("Enter the name of flower : ")
    Flower_list.append(flower_name)

print(f"List of Flowers : {Flower_list}")
'''
#========================================================================================================================
'''
#AIM  : Create a list for ODD and EVEN numbers from the list of N numbers accepted from the user.
#Name : Yash
#Date :

Even_list = []
Odd_list = []

num = int(input("Enter the number : "))

for i in range(num+1):
    if i % 2 == 0:
        Even_list.append(i)
    else:
        Odd_list.append(i)

print(f"Even List : {Even_list} \nOdd list : {Odd_list}")
'''
#========================================================================================================================
'''
#AIM  : To generate a list for N prime numbers. Accept N from the user.
#Name : Yash
#Date :

Prime_list = []

n = int(input("Enter the number : "))

for i in range(2,n+1):
    is_prime = True
    for j in range(2,int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        Prime_list.append(i)

print(f"Prime number list : {Prime_list}")
print(len(Prime_list))      
'''        
#========================================================================================================================
#========================================================================================================================

#PRACTICLE 4
'''

#AIM  : Write a program to implement a tuple in Python for suitable problems. Demonstrate various operations on it.
#Name : Yash
#Date :

#a. Create a tuple for Mobile model name accepted from user
#Accepting moblie model namae from user
mobile_model_name = input("Enter moblie model name : ")
#creating mobile model name tuple
mobile_model_tuple = (mobile_model_name,)
#Displaying tuple
print(f"Moblie model tuple : {mobile_model_tuple}")
print("-------------------------------------------------------------------------------------------------------------\n")

#b. Find the length and index of an element of a tuple.
#creating an tuple
waifus = ("Tsunade","Hinata","Nico robin","Nami","Rias")
print(f"Waifus tuple : {waifus}")
#Length of tuple
print(f"Length of tuple : {len(waifus)}")

#Finding Index of element 'Rias'
print(f"Index of 'Rias' in tuple : {waifus.index("Rias")}")
print("-------------------------------------------------------------------------------------------------------------\n")

#c. Concatenate two tuples.
#Creating two tuples
aot = ("Eren","Mikasa","Armin")
titans = ("Founding","Slayer","colosus")

#Concanating two tuples
tuple_merge = aot + titans
print(f"Aot tuple : {aot} \nTitan tuple : {titans} \nConcatenated tuple : {tuple_merge}")
print("-------------------------------------------------------------------------------------------------------------\n")

#d. Count the occurrence of an item in a tuple
#Default tuple
bleach = ("Ichigo","Orihime","Rengi","Ichigo")
print(f"Bleach tuple : {bleach}")
#Counting the occurence of 'Ichigo' in tuple
print(f"Ichigo count in tuple : {bleach.count("Ichigo")}")
print("-------------------------------------------------------------------------------------------------------------\n")

#e. Access an element in a tuple.
#Creating an default tuple
pokemon = ("charizard","Blastoise","Venasure","Garachop")
print(f"Pokemon tuple : {pokemon}")
#Accessing elements in tuple using index
print(f"Accessing First element of tuple : {pokemon[0]}")
print("-------------------------------------------------------------------------------------------------------------\n")

#f. Check if an element exists in a tuple.
games = ("Bgmi","COC","COD","Valorant")
print(f"Games tuple : {games}")

#checking 'Valorant' element exist in tuple using if_else
if "Valorant" in games:
    print("Valorant exist in tuple")
else:
    print("Valorant does not exist in tuple")
print("-------------------------------------------------------------------------------------------------------------\n")

#g. Iterate through a tuple using a loop.
manhwas = ("Solo leveling","The beginning after the end","The battle god returns")
print(f"Manhwas tuple : {manhwas}")

#Iterating tuple using for loop
for x in manhwas:
    print(x)
print("-------------------------------------------------------------------------------------------------------------\n")

#h. Find the maximum and minimum elements in a tuple of integers.
#Creating a tuple for integers
number_tuple = (1,8,4,6,7,9,4,2,6,10)
print(f"Numner tuple : {number_tuple}")

#Finding max and min element
print(f"Maximum number in tuple : {max(number_tuple)}")
print(f"Minimum number in tuple : {min(number_tuple)}")
print("-------------------------------------------------------------------------------------------------------------\n")

#i. Convert a tuple of strings to a single string.
#Given tuple of strings
string_tuple = ("Hello","world")

#convert tuple to a single string
result = " " . join(string_tuple)
print(result)
print("-------------------------------------------------------------------------------------------------------------\n")

#j. Remove an element from a tuple.
brand_tuple = ("Apple","Samsung","Nike","Adidas")
print(f"Brand tuple : {brand_tuple}")

#converting a tuple to a list
x = list(brand_tuple)
#Removing 'Adida' element
x.remove("Adidas")
#Reconverting a list to tuple
z = tuple(x)
print(f"After removing 'Adidas' from tuple : {z}")
print("-------------------------------------------------------------------------------------------------------------\n")

#k. Find the common elements between two tuples.
tuple1 = (1,2,3,4)
tuple2 = (3,4,5,6)
print(f"Tuple 1 : {tuple1} \nTuple 2 : {tuple2}")
#Finding common element
common_element = set(tuple1) & set(tuple2)
#converting back to tuple
common_tuple = tuple(common_element)
print(f"Common element in tuple : {common_tuple}")
print("-------------------------------------------------------------------------------------------------------------\n")

#l. Sort a tuple of integers.
int_tuple = (3,6,2,8,5,1)
print(f"Int tuple : {int_tuple}")

#Sorting tuple
print(f"Sorted tuple : {sorted(int_tuple)}")
print("-------------------------------------------------------------------------------------------------------------\n")
'''
#========================================================================================================================
'''
#AIM  : Create an interactive program in python to convert a tuple to a list. Create a Project Name tuple. Add the
#       first 5 details then add 5 more. Accept details from the user.
#Name : Yash
#Date :

project_list = []

#Accept the first 5 project details from user
print("Enter the following project details from user")
name = input("Enter your name : ")
subject = input("Enter your subject : ")
class_name = input("Enter your class name : ")
roll_no = input("Enter your roll no. : ")
email = input("Enter Email : ")

#Adding these details to list
project_list.append(name)
project_list.append(subject)
project_list.append(class_name)
project_list.append(roll_no)
project_list.append(email)

#convert list into tuple
project_tuple = tuple(project_list)

#Displaying initial tuple
print(f"Initial tuple of project details : {project_tuple}")

#converting tuple back to list to add more details
project_list = list(project_tuple)

#Accepting the next 5 details
print("\nNow,enter the following details")

project_title = input("Enter project title : ")
aim = input("Enter aim : ")
subject_code = input("Enter subject code : ")
area_of_research = input("Area of research : ")
no_of_group = input("Number of groups : ")

#Addinging the new details to the list
project_list.append(project_title)
project_list.append(aim)
project_list.append(subject_code)
project_list.append(area_of_research)
project_list.append(no_of_group)

project_tuple = tuple(project_list)

print("Final tuple of Project details")
print(f"Project tuple : {project_tuple}")
'''
#========================================================================================================================





















