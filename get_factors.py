#
# www.youtube.com/@mersthub_mentors
#

def get_factors(n):
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)


num = 325

print(get_factors(num))

# [1, 5, 13, 25, 65, 325]