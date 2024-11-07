class FuzzySet:
    def __init__(self, elements, membership_values):
        self.elements = elements
        self.membership_values = membership_values

    # Check if the fuzzy set is normal
    def is_normal(self):
        # A fuzzy set is normal if the maximum membership value is 1
        if max(self.membership_values) == 1:
            return True
        else:
            return False

    # Display the fuzzy set
    def display(self):
        return dict(zip(self.elements, self.membership_values))


# Helper function to take user input for fuzzy set
def input_fuzzy_set():
    elements = input("Enter the elements of the fuzzy set (comma-separated): ").split(",")
    membership_values = list(map(float, input("Enter the membership values (comma-separated): ").split(",")))
    return FuzzySet(elements, membership_values)


# Main program
def perform_operations():
    # Input for fuzzy set
    print("Input for Fuzzy Set:")
    fuzzy_set = input_fuzzy_set()

    # Display the fuzzy set
    print("\nFuzzy Set:", fuzzy_set.display())

    # Check if the fuzzy set is normal
    if fuzzy_set.is_normal():
        print("\nThe fuzzy set is normal.")
    else:
        print("\nThe fuzzy set is not normal.")


# Run the program
perform_operations()
