# Write a python function isPalindrome which accepts a string as an argument and if the
# string is a palindrome it should return True otherwise False.  The function must be
# implemented using loops and no builtin functions / slicing should be used


def isPalindrome(string):
    # Convert the string to lowercase
    string = string.lower()
    
    # Remove all non-alphabetic characters
    string = ''.join(char for char in string if char.isalpha())

    # Check if the string is a palindrome
    for i in range(len(string)//2):
        if string[i] != string[len(string)-i-1]:
            return False
    
    return True
string1 = "racecar"
string2 = "Hello World"
print(isPalindrome(string1)) 
print(isPalindrome(string2))  
