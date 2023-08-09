input_val = {
    'name': 'Arthur'
}


def do_name(name: str):
    print(name)
    return None

print(do_name(**input_val))
