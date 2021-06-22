from number_utility import *


def test_number_utility_reverse_num():
    assert reverse_num(345) == 543


def test_number_utility_sum_of_digits():
    assert sum_of_digits(748) == 19


def test_number_utility_is_prime():
    assert is_prime(17) == True


def test_number_utility_generate_primes():
    assert generate_primes(5, 50) == [
        5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]


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

def test_number_utility_number_of_digits():
    assert number_of_digits(153) == 3

def test_number_utility_is_armstrong():
    assert is_armstrong(1634) == True
    