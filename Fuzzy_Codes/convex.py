class FuzzySet:
    def __init__(self, elements, membership_values):
        self.elements = elements
        self.membership_values = membership_values

    # Check if the fuzzy set is convex
    def is_convex(self):
        n = len(self.elements)
        
        # Check convexity condition for every pair of elements (x1, x2)
        for i in range(n):
            for j in range(i + 1, n):
                x1, x2 = self.elements[i], self.elements[j]
                mu_x1, mu_x2 = self.membership_values[i], self.membership_values[j]

                # Check the convexity condition for the given pair
                for lambda_val in [0.1 * k for k in range(11)]:  # Lambda goes from 0 to 1
                    # Interpolated membership value at the point between x1 and x2
                    interpolated_mu = lambda_val * mu_x1 + (1 - lambda_val) * mu_x2

                    # Convexity condition: interpolated_mu >= min(mu_x1, mu_x2)
                    if interpolated_mu < min(mu_x1, mu_x2):
                        return False  # Not convex if the condition is violated

        return True

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

    # Check if the fuzzy set is convex
    if fuzzy_set.is_convex():
        print("\nThe fuzzy set is convex.")
    else:
        print("\nThe fuzzy set is not convex.")


# Run the program
perform_operations()
