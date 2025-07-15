#simple calculator app using if statement in python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = None

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")

if quotient_result is not None:
    print(f"Quotient: {quotient_result}")
else:
    print("Cannot divide by zero!")

# End of the simple calculator app