import os
def screen_clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
