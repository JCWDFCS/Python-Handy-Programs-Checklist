
def counter(num):
    counter = 0
    while counter <= num:
        print(counter,end=" ")
        counter += 1
    print("\nThe loop has ended.")

def squared_it():
    print("Enter 'exit' when you're done. \n")
    while True:
        data = input('Enter an integer to square: ')
        if data == 'exit':
            break
        i = int(data)
        print(i, 'squared is', i**2, '\n')


def years_value(interest_rate,span):
    investment = 1000
    for i in range(span):
        yearly_interest = investment * interest_rate
        investment = investment + yearly_interest
    investment = round(investment, 2)
    print(investment)


def find_e():
    more = 'y'
    while more == 'y':
        n = int(input('Enter a number: '))
        e = (1 + 1/n) ** n
        print(e)
        more = input('Do you try more(y/n): ')
