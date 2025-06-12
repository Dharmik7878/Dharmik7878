def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero:")
    return a / b

try:
    x=int(input("Enter the first value:"))
    y=int(input("Enter the second value:"))
    result = divide(x,y)
    print("the ans is:",result)

except ValueError as e:
    print(e)
