from statistics import mean


def calculate_mean():
    all_nums = []
    while True:
        num = input('Enter a number: ')
        if num == 'done':
            break
        try:
            all_nums.append(float(num))
        except ValueError:
            print('Bad input')
            continue
    print(sum(all_nums), len(all_nums), mean(all_nums))


calculate_mean()
