import numpy as np

# Fuzzy set class to handle operations on fuzzy sets
class FuzzySet:
    def __init__(self, elements, membership_values):
        self.elements = elements
        self.membership_values = membership_values

    # Union of two fuzzy sets
    def union(self, other):
        result_membership = [max(a, b) for a, b in zip(self.membership_values, other.membership_values)]
        return FuzzySet(self.elements, result_membership)

    # Intersection of two fuzzy sets
    def intersection(self, other):
        result_membership = [min(a, b) for a, b in zip(self.membership_values, other.membership_values)]
        return FuzzySet(self.elements, result_membership)

    # Complement of a fuzzy set
    def complement(self):
        result_membership = [1 - a for a in self.membership_values]
        return FuzzySet(self.elements, result_membership)

    # Difference of two fuzzy sets (A - B = A ∩ B')
    def difference(self, other):
        complement_b = other.complement()
        return self.intersection(complement_b)

    # De Morgan's Law: (A ∪ B)' = A' ∩ B'
    def de_morgan(self, other):
        union_set = self.union(other)
        complement_union = union_set.complement()
        complement_a = self.complement()
        complement_b = other.complement()
        intersection_complement = complement_a.intersection(complement_b)
        return complement_union, intersection_complement

    # Display the fuzzy set
    def display(self):
        return dict(zip(self.elements, self.membership_values))


# Fuzzy Relation class to handle fuzzy relations and composition
class FuzzyRelation:
    def __init__(self, relation_matrix):
        self.relation_matrix = np.array(relation_matrix)

    # Max-min composition of two fuzzy relations
    def max_min_composition(self, other):
        rows_A, cols_A = self.relation_matrix.shape
        rows_B, cols_B = other.relation_matrix.shape
        if cols_A != rows_B:
            raise ValueError("Matrix multiplication not possible due to shape mismatch.")

        result_matrix = np.zeros((rows_A, cols_B))

        for i in range(rows_A):
            for j in range(cols_B):
                result_matrix[i][j] = np.max(np.minimum(self.relation_matrix[i, :], other.relation_matrix[:, j]))

        return FuzzyRelation(result_matrix)

    # Display the fuzzy relation
    def display(self):
        return self.relation_matrix


# Helper function to take user input for fuzzy sets
def input_fuzzy_set():
    elements = input("Enter the elements of the fuzzy set (comma-separated): ").split(",")
    membership_values = list(map(float, input("Enter the membership values (comma-separated): ").split(",")))
    return FuzzySet(elements, membership_values)


# Helper function to take user input for fuzzy relations
def input_fuzzy_relation():
    rows = int(input("Enter the number of rows in the fuzzy relation matrix: "))
    cols = int(input("Enter the number of columns in the fuzzy relation matrix: "))
    print("Enter the relation matrix row by row (values separated by space):")
    relation_matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        relation_matrix.append(row)
    return FuzzyRelation(relation_matrix)


# Main program
def perform_operations():
    # Input for fuzzy sets A and B
    print("Input for Fuzzy Set A:")
    A = input_fuzzy_set()
    print("Input for Fuzzy Set B:")
    B = input_fuzzy_set()

    # Union of A and B
    union_result = A.union(B)
    print("\nUnion of A and B:", union_result.display())

    # Intersection of A and B
    intersection_result = A.intersection(B)
    print("\nIntersection of A and B:", intersection_result.display())

    # Complement of A
    complement_a_result = A.complement()
    print("\nComplement of A:", complement_a_result.display())

    # Complement of B
    complement_b_result = B.complement()
    print("\nComplement of B:", complement_b_result.display())

    # Difference (A - B)
    difference_result = A.difference(B)
    print("\nDifference (A - B):", difference_result.display())

    # De Morgan’s Law
    complement_union_result, intersection_complement_result = A.de_morgan(B)
    print("\nDe Morgan's Law - Complement of (A ∪ B):", complement_union_result.display())
    print("De Morgan's Law - (A' ∩ B'):", intersection_complement_result.display())

    # Input for fuzzy relations
    print("\nInput for Fuzzy Relation R1:")
    R1 = input_fuzzy_relation()
    print("Input for Fuzzy Relation R2:")
    R2 = input_fuzzy_relation()

    # Max-min composition of fuzzy relations R1 and R2
    composition_result = R1.max_min_composition(R2)
    print("\nMax-min composition result:")
    print(composition_result.display())


# Run the program
perform_operations()
