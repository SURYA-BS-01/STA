def check_odd_even(number):
    return "Even" if number % 2 == 0 else "Odd"

# Test cases
numbers = [2, 7, 0, -4]
for num in numbers:
    result = check_odd_even(num)
    print(f"Number: {num}, Result: {result}")
