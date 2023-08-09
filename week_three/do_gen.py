"""
write a function that yields the first 10 prime numbers.
"""


def is_prime_number(input_no: int):
    if input_no > 1:
        for i in range(2, int(input_no/2)+1):
            if (input_no % i) == 0:
                return False
            return True
    else:
        return False


def gen_prime_numbers():
    count = 0
    value = 1
    while count < 10:
        if is_prime_number(value):
            yield value
            count += 1
        value += 1

for i in gen_prime_numbers():
    print(i)
