def grade_number(num: float = 0) -> str:
    if num < 0.6:
        return 'F'
    elif num >= 0.9:
        return 'A'
    elif num >= 0.8:
        return 'B'
    elif num >= 0.7:
        return 'c'
    else:
        return 'D'


def get_user_input():
    user_input = input('Input the grade \n')
    try:
        input_grade = float(user_input)
    except ValueError:
        print('Grade should be an int or float')
        return
    if input_grade > 1:
        print('Maximum input is 1')
        return
    print(f'Grade: {grade_number(input_grade)}')
    return

get_user_input()
