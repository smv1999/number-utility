Introduction
============

The number-utility module makes it simple for you to do number manipulation and perform various operations on numbers.

reverse_num(num)
===============

Returns an integer : Reverse of a number passed as argument

For **Example**

>>> from number_utility import reverse_num
num = 345
print(reverse_num(num))

**Output**::

  543

sum_of_digits(num)
=================

Returns an integer : Sum of the digits of a number passed as argument

For **Example**

>>> from number_utility import sum_of_digits
num = 345
print(sum_of_digits(num))

**Output**::

  12
  
is_prime(num)
============

Returns a boolean : Checks whether the number passed as input is prime or composite

For **Example**

>>> from number_utility import is_prime
num = 17
print(is_prime(num))

**Output**::

  True
