# 1. Print First 10 natural numbers using while loop
#    Expected output:
#     1
#     2
#     3
#     4
#     5
#     6
#     7
#     8
#     9
#     10
def print10naturals():
    num = 1
    while num != 11:
        print(num)
        num = num +1


# 2. Write a program to print the following number pattern using a loop
#    Expected Output:
#     1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5
def numberspyramide(iterations = 5):
    for i in range(0,iterations):
        for j in range(1, i+2):
            print(j, end="")
        print("\r")

# 3. Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
#    For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
#    Expected Output:
#          Enter number 10
#          Sum is:  55
def sumtillnum(num=10,sum=0):
    numholder = num
    if numholder == 0:
        return sum
    else:
        sum = numholder + sumtillnum(numholder - 1, sum)
        return sum
print(sumtillnum())

# 4. Print list in reverse order using a loop
#    Given: list1 = [10, 20, 30, 40, 50]
#    Expected output:
#       50
#       40
#       30
#       20
#       10
def listreversing(list = [1,2,3,4,5,6,7,8,9,10,11]):
    # listlen = len(list)
    # while listlen != 0:
    #     print(list[listlen-1])
    #     listlen = listlen - 1
    # OR
    for i in list[::-1]: print(i) # Oneliner is better :)

