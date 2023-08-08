def upper_case(input_str):
    output = [char.upper() for char in input_str]
    return "".join(output)

print(upper_case("this is the string"))


def list_length(input_str):
    return [len(i) for i in input_str.split(' ')]

print(list_length("this is the string"))
