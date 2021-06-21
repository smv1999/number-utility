from number import *


def test_number_reverse_num():
    assert reverse_num(345) == 543


def test_number_sum_of_digits():
    assert sum_of_digits(748) == 19


def test_number_is_prime():
    assert is_prime(17) == True


def test_number_generate_primes():
    assert generate_primes(2, 10) == [2, 3, 5, 7]


def test_number_gcd():
    assert gcd(12, 60) == 12


def test_number_lcm():
    assert lcm(5, 6) == 30


def test_number_get_factors():
    assert get_factors(10) == [1, 10, 2, 5]


def test_number_factorial():
    assert factorial(6) == 720
