x = int(input("Enter a positive integer: "))

if x < 0:
    x = 0
    print("x changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("x is 1")
else:
    print("x is greater than 1")

