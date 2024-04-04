
# Input a list of Numbers from user i.e take integer inputs and append to list.
x = [int(x) for x in input("Enter value: ").split()]
print(x)

#Find the smallest and Second Smallest Numbers from that list

def find_length(x):
    lenth = len(x)
    x.sort()
    print("smallest Number is:", x[0])
    print("second smallest Number is:", x[1])

x = [int(x) for x in input("Enter value: ").split()]
print(x)
smallest = find_length(x)



