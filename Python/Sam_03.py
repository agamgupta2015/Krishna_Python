# Write a program that computes the sum of n terms of following series.
# 12 - 22 + 32 - 42 + ... + n


n = int(input("Enter the number of terms: "))
sum = 0
sign = 1

for i in range(1, n+1):
    term = i**2 * sign
    sum += term
    sign *= -1

print("The sum of the series is:", sum)
