
def calculate_future_value(month_investment, year_interest_rate, years=20):
    #convert the yearly values to monthly values.
    print('Entering calculate_future_value()')
    month_interest_rate = year_interest_rate / 12 / 100
    months = years * 12
    #calculate future value
    future_value = 0.0
    for i in range(0, months):
        month_interest_amount = future_value * month_interest_rate
        future_value += month_investment
        future_value += month_interest_amount
        print('i = ', i+1,'future value = ',round(future_value,2))
    return future_value

def get_float(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("You entered an invalid integer.")
            continue
        if number > low and number <= high:
            is_valid = True # identifier
            return number
        else:
            print("Entry must be greater than " + str(low)
                  + " and less than or equal to " + str(high) + ".")

def get_integer(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("You entered an invalid integer.")
            continue
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print("Entry must be greater than " + str(low)
                  + " and less than or equal to " + str(high) + ".")

def main():
    choice = 'y'
    while choice.lower() == 'y':
        #get input from the user.
        month_investment = get_float("Enter monthly investment:\t", 0, 1000)
        year_interest_rate = get_float("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)


        future_value = calculate_future_value(month_investment, year_interest_rate, years)
        print('Future value:\t\t\t' + str(round(future_value, 2)))
        print()

        choice = input("Continue? (y/n): ")
    print('Bye!')

if __name__ == "__main__":
     main()
