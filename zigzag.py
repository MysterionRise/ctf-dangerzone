import itertools

def is_valid_permutation(perm):
    n = len(perm)
    for i in range(2, n + 1):
        if i % 2 == 0:
            # i is even, a[i-1] should be > a[i]
            if perm[i - 2] < perm[i - 1]:
                return False
        else:
            # i is odd, a[i-1] should be < a[i]
            if perm[i - 2] > perm[i - 1]:
                return False
    return True

def count_valid_permutations(n):
    MOD = 10**9 + 7
    count = 0
    for perm in itertools.permutations(range(1, n + 1)):
        if is_valid_permutation(perm):
            count = (count + 1) % MOD
    return count

# Example usage:
for n in range(1, 1000):
    print(count_valid_permutations(n))
