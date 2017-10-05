
def counter():
    counter = 0
    while counter < 5:
        print(counter,end=" ")
        counter += 1
    print("\nThe loop has ended.")

def squaredIt():
    print("Enter 'exit' when you're done. \n")
    while True:
        data = input('Enter an integer to square:')
        if data == 'exit':
            break
        i = int(data)
        print(i, 'squared is', i**2, '\n')


def yearsValue():
    investment = 1000
    for i in range(20):
        yearlyInterest = investment * 0.05
        investment = investment + yearlyInterest
    investment = round(investment, 2)
    print(investment)


def findE():
    more = 'y'
    while more == 'y':
        n = int(input('Enter a number: '))
        e = (1 + 1/n) ** n
        print(e)
        more = input('Do you try more(y/n): ')
