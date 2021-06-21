def reverse_num(num):
    """Returns an integer

    Reverse of a number passed as argument
    """
    rev = 0
    while num > 0:
        rev = (rev * 10) + (num % 10)
        num //= 10
    return rev


def sum_of_digits(num):
    """Returns an integer

    Sum of the digits of a number passed as argument
    """
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s


def is_prime(num):
    """Returns a boolean 

    Checks whether the number passed as argument is a prime or composite number
    """
    if num == 0 or num == 1:
        return False
    i = 2
    while i*i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def generate_primes(num1, num2):
    """Returns a list

    Prime numbers generated between the given range(num1, num2)
    """
    if num1 > num2:
        raise Exception(
            "num1 can't be greater than num2. Specify the correct range.")
    if num1 == 0 or num2 == 0:
        raise Exception("Specify the correct range.")
    if num1 == 1:
        num1 = 2
    primes_generated = []
    range_length = num2 - num1 + 1
    primes = [True for i in range(range_length)]
    inc_value = num1
    while inc_value * inc_value <= num2:
        if primes[inc_value] == True:
            for i in range(inc_value * inc_value, range_length, inc_value):
                primes[i] = False
        inc_value += 1
    for prime in range(num1, range_length):
        if primes[prime]:
            primes_generated.append(prime)
    return primes_generated


def gcd(num1, num2):
    """Returns an integer

    Greatest common divisor of the two numbers passed as arguments
    """
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


def lcm(num1, num2):
    """Returns an integer

    Least common multiple of the two numbers passed as arguments
    """
    return num1 * num2 // gcd(num1, num2)


def get_factors(num):
    """Returns a list

    Factors of the number passed as argument
    """
    factors = []
    inc_value = 1
    while inc_value * inc_value <= num:
        if num % inc_value == 0:
            if num//inc_value == inc_value:
                factors.append(inc_value)
            else:
                factors.append(inc_value)
                factors.append(num//inc_value)
        inc_value += 1
    return factors


def factorial(num):
    """Returns an integer

    Factorial of the number passed as argument
    """
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact
