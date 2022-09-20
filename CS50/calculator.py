try:
    x = int(input("x: "))

except ValueError:
    print("That's is not an int!")
    exit()

try:
    y = int(input("y: "))

except ValueError:
    print("That's is not an int!")
    exit()

z = x/y 


print(x+y)
print(z)
print(f"{z:.50}")

