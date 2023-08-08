import re

should_match = "1.23"
should_not_match = "1.234"

pattern = re.compile(r'^[0-9]+[.][0-9]{2}$')
print(pattern.search(should_match))
print(pattern.match(should_not_match))


# date_str = "03/01/2021"
# match = re.search(r'^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$', date_str)


