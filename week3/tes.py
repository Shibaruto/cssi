num = int(raw_input("Enter a number: "))
if num > 0:
    print("That's a positive number!")
elif num < 0:
    print("That's a negative number!")
else:
    print("zero is neither positive nor negative")

x = 20
if x > 18:
    print("You can buy lottery tickets!")
    if x > 25:
        print("You can also rent a car!")
    print("And you can get your own credit card!")
print("End program")

for i in range(5):
    print(i)
for i in [0,1,2,3,4]:
    print(i)
name = "Brooklyn"
for i in range(5,1,-1):
    print(name[i])
