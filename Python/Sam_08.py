# Write a menu driven python program to perform the following operations:
# 1. create set A and set B from user input. (input at least 5 elements in each set)
# 2. perform symmetric difference : A ^ B
# 3. perform union operation: A | B
# 4. Perform intersection operation: A & B

def create_set():
    """Helper function to create a set from user input"""
    elements = input("Enter the elements of the set, separated by spaces: ")
    elements = elements.split()
    return set(elements)


def symmetric_difference(A, B):
    """Helper function to compute the symmetric difference of two sets"""
    return A ^ B


def union(A, B):
    """Helper function to compute the union of two sets"""
    return A | B


def intersection(A, B):
    """Helper function to compute the intersection of two sets"""
    return A & B


# Main program loop
while True:
    print("\nMenu:")
    print("1. Create sets A and B")
    print("2. Compute symmetric difference: A ^ B")
    print("3. Compute union: A | B")
    print("4. Compute intersection: A & B")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Create sets A and B from user input
        print("Enter the elements of set A:")
        A = create_set()
        print("Enter the elements of set B:")
        B = create_set()
        print(f"Set A: {A}")
        print(f"Set B: {B}")
    elif choice == "2":
        # Compute symmetric difference A ^ B
        if 'A' in locals() and 'B' in locals():
            sym_diff = symmetric_difference(A, B)
            print(f"Symmetric difference of A and B: {sym_diff}")
        else:
            print("Please create sets A and B first")
    elif choice == "3":
        # Compute union A | B
        if 'A' in locals() and 'B' in locals():
            set_union = union(A, B)
            print(f"Union of A and B: {set_union}")
        else:
            print("Please create sets A and B first")
    elif choice == "4":
        # Compute intersection A & B
        if 'A' in locals() and 'B' in locals():
            intersection = intersection(A, B)
            print(f"Intersection of A and B: {intersection}")
        else:
            print("Please create sets A and B first")
    elif choice == "5":
        # Exit the program
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
