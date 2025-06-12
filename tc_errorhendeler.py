try:
    number =int(input("Enter the number:"))
    result = 10 / number
    print(f"result: {result}")

except ZeroDivisionError as e:
    print("Error cannot divide by Zero:")
except ValueError as e:
    print("Erro Invalid input. Please enter a valid number.")
finally:
    print("Thank you")
