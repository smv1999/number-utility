## number-utility

![GitHub followers](https://img.shields.io/github/followers/smv1999?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/smv1999/number-utility?style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/smv1999/number-utility?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/smv1999/number-utility?style=for-the-badge)

### Introduction 

The number-utility module makes it simple for you to do number manipulation and perform various operations on numbers. 

### Installation 

You can install the module using pip as shown below.

```bash
pip install number-utility
```
### Usage

Consider the following examples :

```python
from number_utility import *

num1 = 12
num2 = 60

print(gcd(num1, num2))
#Output - 12
```

```python
from number_utility import *

start = 2
end = 10

print(generate_primes(start, end))
#Output - [2, 3, 5, 7]
```

### Testing 

To install number-utility, along with the tools you need to develop and run tests. Run the following command :
```bash
$ pip install -e .[dev]
```

For running the tests, type the following command :

```bash
py.test
```

### Bugs/Requests 

Please use the [GitHub issue tracker](https://github.com/smv1999/number-utility/issues) to submit bugs or request features.

### License 

Copyright Vaidhyanathan S M, 2021

Distributed under the terms of the [MIT](https://github.com/smv1999/number-utility/blob/main/LICENSE) license, number-utility is free and open source software.


