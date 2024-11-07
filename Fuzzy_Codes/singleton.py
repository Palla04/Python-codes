class FuzzySet:
    def __init__(self, elements, membership_values):
        self.elements = elements
        self.membership_values = membership_values

    # Check if the fuzzy set is a singleton
    def is_singleton(self):
        # A fuzzy set is a singleton if there is exactly one element with a membership value of 1
        ones_count = self.membership_values.count(1)
        if ones_count == 1 and all(m < 1 for m in self.membership_values if m != 1):
            return True
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

    # Check if the fuzzy set is a singleton
    if fuzzy_set.is_singleton():
        print("\nThe fuzzy set is a singleton.")
    else:
        print("\nThe fuzzy set is not a singleton.")


# Run the program
perform_operations()
