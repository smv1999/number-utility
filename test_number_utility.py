from number_utility import *


def test_number_utility_reverse_num():
    assert reverse_num(345) == 543


def test_number_utility_sum_of_digits():
    assert sum_of_digits(748) == 19


def test_number_utility_is_prime():
    assert is_prime(17) == True


def test_number_utility_generate_primes():
    assert generate_primes(2, 10) == [2, 3, 5, 7]


def test_number_utility_gcd():
    assert gcd(12, 60) == 12


def test_number_utility_lcm():
    assert lcm(5, 6) == 30


def test_number_utility_get_factors():
    assert get_factors(10) == [1, 10, 2, 5]


def test_number_utility_factorial():
    assert factorial(6) == 720

def test_number_utility_fibonacci():
    assert fibonacci(6) == 5