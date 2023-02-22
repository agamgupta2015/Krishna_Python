# Write a python function to count words and vowels present in string passed as an
# argument.

def count_words_vowels(string):
    word_count = len(string.split())
    vowel_count = 0
    vowels = "aeiouAEIOU"
    
    for char in string:
        if char in vowels:
            vowel_count += 1
    
    return word_count, vowel_count
    
string =input("Enter any string :")
word_count, vowel_count = count_words_vowels(string)
print("Number of words:", word_count)
print("Number of vowels:", vowel_count)
