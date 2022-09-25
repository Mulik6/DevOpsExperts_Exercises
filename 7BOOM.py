
def seven_boom(range_to_count=100):
    arr = []
    for i in range(range_to_count):
        if (i % 7) != 0:
            arr.append(i)
        elif i != 0:
            arr.append("BOOM!")
    print(arr)


def divisible_by_seven(range_to_count=100):
    arr = []
    for i in range(range_to_count):
        if (i % 7) == 0:
            arr.append(i)
    print(arr)



print("------ 7 BOOM ------")
seven_boom(100)

print("------divisible_by_seven---------")
divisible_by_seven(100)
