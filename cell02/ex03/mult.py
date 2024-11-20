beam1 = float(input("Enter the first number:\n "))
beam2 = float(input("Enter the second number:\n "))
result = beam1 * beam2
print(f"{beam1} x {beam2} = {result}")
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
