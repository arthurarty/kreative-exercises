from typing import Optional, Tuple


def compute_gross_pay(no_hours: float, hourly_rate: float) -> float:
    if no_hours <= 40:
        return no_hours * hourly_rate
    extra_pay = (no_hours - 40) * (hourly_rate * 1.5)
    return (40 * hourly_rate) + extra_pay


def collect_user_input() -> Optional[Tuple[float, float]]:
    employee_hours = input("Enter Hours: ")
    rate = input("Enter Rate: ")
    try:
        return float(employee_hours), float(rate)
    except ValueError:
        print('Values entered must be integers or float')
        return None
    
user_input = collect_user_input()
if user_input:
    print(f'Gross Pay: {compute_gross_pay(user_input[0], user_input[1])}')
