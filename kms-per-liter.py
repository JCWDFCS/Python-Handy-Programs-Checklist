#The kilometers Per Liter program
#Display the title.
def display_menu():
    print("The Kilometers Per Liter Program")
    print("=============================================")

#get input from the user.
def get_entries():
    while True:
        try:
            liters_used = float(input('Please enter liters of gas used:\t'))
            break
        except ValueError:
            print('Entries must be numbers. Please try again.')
            continue

    while True:
        try:
            kms_driven = float(input('Please enter kilometers driven: \t'))
            break
        except ValueError:
            print('Entries must be numbers. Please try again.')
            continue
    while True:
        try:
            cost_per_liter = float(input('Please enter cost per liter: \t\t'))
            break
        except ValueError:
            print('Entries must be numbers. Please try again.')
            continue

    return liters_used, kms_driven, cost_per_liter

def calculate_results(liters_used, kms_driven, cost_per_liter):
    #calculate and round kilometers per liter.
    km_per_liter = kms_driven / liters_used
    cost_per_km = liters_used * cost_per_liter / kms_driven
    km_per_liter = round(km_per_liter,2)
    cost_per_km = round(cost_per_km,2)
    return km_per_liter, cost_per_km

def main():
    display_menu()
    liters_used, kms_driven, cost_per_liter = get_entries()
    km_per_liter, cost_per_km = calculate_results(liters_used, kms_driven, cost_per_liter)
    # display the result
    print("=============================================")
    print("Kilometers Per Liter: \t\t\t" + str(km_per_liter))
    print("Cost Per Kilometer: \t\t\t" + str(cost_per_km))
    print()
    print('Bye')





if __name__ == '__main__':
    main()
