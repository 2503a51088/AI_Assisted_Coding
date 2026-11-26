
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Testing multiple inputs
numbers = [2, 5, 7, 10, 15, 17, 20, 1]

for num in numbers:
    print(num, ":", is_prime(num))
