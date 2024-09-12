def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
        return result
    
def permutations(n, r):
    return factorial(n) // factorial(n-r)

def combinations(n,r):
    return factorial(n) // (factorial(r)*factorial(n-r))

n = int(input("Enter n :"))
r = int(input("Enter r :"))

print(f"Permutation {n}P{r} : ", permutations(n,r))
print(f"Combinations of {n}C{r} : ", combinations(n,r))