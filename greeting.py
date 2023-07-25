def handle_greeting(input_greeting: str):
    print(f'{input_greeting} \nHow are you feeling?')
    feeling = input()
    print('I am happy to hear that you are feeling ' + feeling + '.')

greetings = ['Good morning!', 'Good afternoon!', 'Good evening!']
for greeting in greetings:
    handle_greeting(greeting)
