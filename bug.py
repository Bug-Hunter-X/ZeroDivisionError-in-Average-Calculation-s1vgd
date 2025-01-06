def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    return total / len(numbers) # potential ZeroDivisionError

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10,20,30]
average = calculate_average(my_numbers)
print(f"The average is: {average}")