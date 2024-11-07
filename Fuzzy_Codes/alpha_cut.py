class FuzzySet:
    def __init__(self, elements, membership_values):
        self.elements = elements
        self.membership_values = membership_values

    # Find the alpha-cut of the fuzzy set
    def alpha_cut(self, alpha):
        # Check that the alpha value is between 0 and 1
        if not (0 <= alpha <= 1):
            print("Alpha value must be between 0 and 1.")
            return None
        
        # Perform the alpha-cut: include elements where membership value is >= alpha
        alpha_cut_set = {self.elements[i] for i in range(len(self.membership_values)) if self.membership_values[i] >= alpha}
        return alpha_cut_set

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

    # Get the alpha value for the alpha-cut
    alpha = float(input("\nEnter the alpha value (between 0 and 1): "))

    # Find and display the alpha-cut
    alpha_cut_result = fuzzy_set.alpha_cut(alpha)
    if alpha_cut_result is not None:
        print(f"\nThe alpha-cut of the fuzzy set at alpha = {alpha} is: {alpha_cut_result}")


# Run the program
perform_operations()
