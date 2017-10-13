from datetime import datetime,date
import locale

# type_based dispatch


def get_arrival_date():
    while True:
        date_str = input('Enter arrival date (YYYY-MM-DD): ')
        try:
            arrival_date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print('Invalid date format. Try again.')
            continue
        #strip non-zero time values from datetime object
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        if arrival_date < today:
            print('Arrival date must be today or later. Try again.')
            continue
        else:
            return arrival_date

def get_departure_date():
    while True:
        date_str = input('Enter departure date (YYYY-MM-DD):')
        try:
            departure_date = datetime.strptime(date_str, '%Y-%m-%d') #validate
            now = datetime.now()
            today = datetime(now.year, now.month, now.day)
            if departure_date <= today:
                print('Daparture date must be after arrival date. Try again.')
                continue
            else:
                return departure_date
        except ValueError:
            print('Invalid date format. Try again.')


def main():
    print('The Hotel Reservation Program\n')
    while True:
        #get datetime from user
        arrival_date = get_arrival_date()
        departure_date = get_departure_date()
        print()

        #calculate nights and costs
        rate1 = 85.0
        rate2 = 105.0
        rate_message = ''
        if arrival_date.month == 8 and departure_date== 8: #August is hign season.

            rate_message = '(Hign season in August)'
            total_nights = (departure_date - arrival_date).days
            total_cost = rate2 * total_nights
        elif arrival_date.month == 8 and departure_date != 8:
            rate_message = '(Hign season in August)'
            days_in_August = 31 - arrival_date.day + 1
            days_out_August = (departure_date - arrival_date).days - days_in_August
            total_nights = (departure_date - arrival_date).days
            total_cost = rate2 * days_in_August + rate1 * days_out_August
        else:
            total_nights = (departure_date - arrival_date).days
            total_cost = rate1 * total_nights





        #format results
        date_format = '%B %d, %Y'
        locale.setlocale(locale.LC_ALL, '')

        print('Arrival Date:   ', arrival_date.strftime(date_format))
        print('Departure Date: ', departure_date.strftime(date_format))
        print('Nightly rate:   ', locale.currency(rate1), rate_message)
        print('Total Nights:   ', total_nights)
        print('Total Price:    ', locale.currency(total_cost))
        print()
        print('Datetime:       ',datetime.now())

        #check whether the user wants to continue
        choice = input('Continue? (y/n): ')
        print()
        if choice.lower() != 'y':
            print('Bye...')
            break



if __name__ == '__main__':
    main()
