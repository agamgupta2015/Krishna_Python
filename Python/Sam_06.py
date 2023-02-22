# Write a python program to display the count of words having length n, present in a text
# file 'Sample.txt'. The value of n must be received from user input. Handle appropriate
# exceptions.

filename = 'Sample.txt'

try:
    # Prompt user for word length to search for
    n = int(input("Enter word length to search for: "))
    
    # Open the file for reading
    with open(filename, 'r') as file:
        # Initialize word count
        count = 0
        
        # Loop over each line in the file
        for line in file:
            # Split the line into words
            words = line.strip().split()
            
            # Loop over each word in the line
            for word in words:
                # Check if the length of the word matches n
                if len(word) == n:
                    count += 1
        
        # Print the word count
        print(f"Number of words with length {n}: {count}")
        
except FileNotFoundError:
    print(f"Error: {filename} not found.")
    
except ValueError:
    print("Error: Invalid input. Please enter a positive integer for word length.")
