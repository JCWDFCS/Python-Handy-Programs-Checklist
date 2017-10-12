import os
os.chdir('/Users/gaowei/Documents/Diary/Python-Handy-Programs-Checklist')

import temperature as temp

def display_menu():
    print('MENU')
    print('1. Fahrenheit to Celsius')
    print('2. Celsius to Fahrenheit')
    print()

def convert_temp():
    option = int(input("Enter a menu option:\t\t"))
    if option == 1:
        f = int(input('Enter degrees Fahrenheit: '))
        c = round(temp.to_celsius(f), 2)
        print('Degree Celsius:\t\t', c)
    elif option == 2:
        c = int(input("Enter degree Celcius: \t\t"))
        f = round(temp.to_fahrenheit(c), 2)
        print('Degree Fahrenheit:\t\t', f)
    # guardian
    else:
        print('You must enter a valid menu number.')

def main():
    display_menu()
    again = 'y'
    while again.lower() == 'y':
        convert_temp()
        print()
        again = input("Convert another temperature? (y/n): ")
        print()
    print('Bye!')

if __name__ == '__main__':
    main()
