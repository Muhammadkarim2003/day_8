def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Tub son")
    else:
        print("Tub son emas")

n = int(input())
prime_checker(number=n)