'''
This module contains functions for converting temperature between degrees Fahrenheit and
degress Celsius.
'''

def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
# the main() function is used to test the other functions
# this code isn's run if this module isn't the main Modules

def main():
    for temp in range(0, 212, 40):
        print(temp, 'Fahrenheit =', round(to_celsius(temp)), 'Celsius')

    for temp in range(0, 100, 20):
        print(temp, 'Celcius =', round(to_fahrenheit(temp)), 'Fahrenheit')

if __name__ == "__main__":
    main()
