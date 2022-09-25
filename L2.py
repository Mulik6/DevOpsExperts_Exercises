# 1.
def bigorsmall(x,y):
    if x>y:
        print(x)
    elif y<x:
        print("small")

# 2.
def printiterations(i=5):
    for x in range(i):
        print(x)

# 3.
def numtoseason(num=1):
    if num==1:
        print("summer")
    elif num==2:
        print("winter")
    elif num == 3:
        print("fall")
    elif num == 4:
        print("spring")
    else:
        print("no season for the number you entered.")

# 4.
# a. the loop will run 10 times statring from 1 to 10.
# b. 10

# 5.
def stam(age=31,fnfl="K",currentdollarcur =3.2,everfly = True, apartment = 4):
    print(f"Your age: {age}, Your Last name first letter: {fnfl}, Current $ for NIS: {currentdollarcur}, Ever flew?: {everfly}, Your apartment #{apartment}")
    print(f"Your age+current $ to NIS currency: {currentdollarcur+age}")

# 6.
def phonenumberfetcher():
    phonenumber= input("Enter your phone numbrer: ")
    print(f"phone number: {phonenumber}")

# 7.
def print_hello():
    print("hello")
def calculate():
    print(f"{5+3.2}")

# 8.
def fetchname():
    name = input("Enter your name: ")
    print(f"Your name: {name}")
def divbytwo():
    num = input("Enter a number: ")
    print(f"Divided by two: {num/2}")

# 9.
def sum(x=1,y=1):
    print(f"{x+y}")
def my_concat(str1="Muli", str2="Kozak"):
    newstr = f"{str1} {str2}"
    return newstr

# 10.
def pyramide(char="*",iterations = 10):
    for i in range(0,iterations):
        for j in range(0, i+1):
            print(f"{char}", end="")
        print("\r")

# 11.
def bigaxe(char="*", rows=7):
    for i in range(0, rows):
        for j in range(0, rows):
            if (i == j or (j == rows - 1 - i)):
                print(f'{char}', end='')
            else:
                print(' ', end='')
        print()

# 12.
# a.
def fetchnumber():
    num = input("Enter a numbrer: ")
    return num
# b.
def digsum():
    num = fetchnumber()
    dig_sum = 0

    for i in range(0, len(str(num))):
        dig_sum = dig_sum + int(str(num)[i-1])
    print(dig_sum)

