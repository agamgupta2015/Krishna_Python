# Write a python program which accepts only a three-digit number from the user and
# 1. Print the reverse of the number
# 2. Calculate and print the sum of digits
# 3. If a user enters a number other than a three-digit number the program should
# display an invalid input message


# Prompt user for a three-digit number
num = input("Enter a three-digit number: ")

# Check if input is a three-digit number
if not num.isdigit() or len(num) != 3:
    print("Invalid input: please enter a three-digit number.")
else:
    # Reverse the number and print it
    rev_num = num[::-1]
    print(f"Reverse of the number: {rev_num}")

    # Calculate and print the sum of digits
    sum_digits = sum(int(digit) for digit in num)
    print(f"Sum of digits: {sum_digits}")
