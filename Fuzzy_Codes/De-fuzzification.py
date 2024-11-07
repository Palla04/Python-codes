class FuzzySet:
    def __init__(self, elements, membership_values):
        self.elements = elements
        self.membership_values = membership_values

    # Maxima method
    def maxima_method(self):
        max_membership_value = max(self.membership_values)
        max_index = self.membership_values.index(max_membership_value)
        return self.elements[max_index]

    # Centroid method
    def centroid_method(self):
        numerator = sum([self.membership_values[i] * float(self.elements[i]) for i in range(len(self.elements))])
        denominator = sum(self.membership_values)
        return numerator / denominator if denominator != 0 else 0

    # Weighted average method
    def weighted_average_method(self):
        numerator = sum([self.membership_values[i] * float(self.elements[i]) for i in range(len(self.elements))])
        denominator = sum(self.membership_values)
        return numerator / denominator if denominator != 0 else 0

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

    # Perform Maxima Method
    print("\nMaxima Method Result:", fuzzy_set.maxima_method())

    # Perform Centroid Method
    print("\nCentroid Method Result:", fuzzy_set.centroid_method())

    # Perform Weighted Average Method
    print("\nWeighted Average Method Result:", fuzzy_set.weighted_average_method())


# Run the program
perform_operations()
