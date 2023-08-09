"""
Write a decorator that converts the result of a function to uppercase.
"""


def upper_case_decorator(func):
    def upper_case(*args, **kwargs):
        returned_value = func(*args, **kwargs)
        return returned_value.upper()
    return upper_case


@upper_case_decorator
def replace_spaces(input_str: str):
    return input_str.replace(' ', '*')


# print(replace_spaces('Going to school'))


"""
Write a decorator that repeats the output of a function a specified number of times.
"""

def repeat_output(func):
    def _repeat(*args, **kwargs):
        output = func(*args, **kwargs)
        for _ in range(3):
            print(output)
        return output
    return _repeat

@repeat_output
def hello_world():
    return "hello world"

hello_world()
