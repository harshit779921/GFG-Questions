class Solution:
    def print_divisors(self, N):
        from math import sqrt
        small = []
        large = []

        for i in range(1, int(sqrt(N)) + 1):
            if N % i == 0:
                small.append(i)
                if i != N // i:      # avoid duplicate for perfect squares
                    large.append(N // i)

        for x in small:
            print(x, end=" ")

        for x in reversed(large):
            print(x, end=" ")