#The kilometers Per Liter program
#Display the title.
import pickle
filename = 'trips.bin'


def display_menu():
    print("The Kilometers Per Liter Program")
    print()


def write_trip(trips):
    #get input from the user.
    with open(filename,'wb') as file:
        pickle.dump(trips, file)


def read_trips(filename):
    trips = []
    with open(filename,'rb') as file:
        try:
            trips = pickle.load(file)
        except (EOFError):
            pass
    return trips



def add_a_trip(trips):
    trip = []
    kms_driven = float(input('Enter kilometers driven: \t'))
    liters_used = float(input('Enter liters of gas used:\t'))
    cost_per_liter = float(input('Enter cost per liter: \t\t'))
    #Computing
    km_per_liter = round(kms_driven / liters_used, 2)
    cost_per_100kms = round(liters_used * cost_per_liter / kms_driven * 100, 2)

    print('Kms Per Liter: \t\t\t' + str(km_per_liter))
    print('Cost Per 100Kms:\t\t' + str(cost_per_100kms))
    print()
    trip.append(kms_driven)
    trip.append(liters_used)
    trip.append(cost_per_liter)
    trip.append(km_per_liter)
    trip.append(cost_per_100kms)
    trips.append(trip)
    # write into file
    write_trip(trips)


# def deletetrip(trips):
#     index = int(input('Number: ')
#     trips.pop(index - 1)
#     write_trip(trips)

def list_trips(trips):
    print('Distance\t' + 'Liters\t\t' + 'cost_per_liter\t' +'km_per_liter\t'+ 'cost_per_100kms')
    for i in range(len(trips)):
        trip = trips[i]
        print('%s\t\t %s\t\t %s\t\t %s\t\t %s\t\t' %(trip[0],trip[1],trip[2],trip[3],trip[4]))
    print()


def main():
    display_menu()
    option = 'y'
    while option == 'y':
        trips = read_trips(filename)
        print(trips)
        list_trips(trips)
        print()
        add_a_trip(trips)
        list_trips(trips)
        option =input('More entries? (y or n): ')
        print()


if __name__ == '__main__':
    main()
