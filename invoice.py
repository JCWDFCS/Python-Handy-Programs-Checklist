
from datetime import datetime,timedelta
format_str = '%Y-%m-%d'
def get_invoice_date():
    while True:
        invoice_date_str = input('Enter invoice date(YYYY-MM-DD): ')
        try:
            invoice_date = datetime.strptime(invoice_date_str, format_str)
        except ValueError:
            print('Invalid data format! Try agian.')
            continue
        if invoice_date > datetime.now():
            print("Invoice date must be today or earlier.Try again.")
            continue
        else:
            return invoice_date



def main():
    print("The Invoice Due Date Program")
    print()

    while True:

        invoice_date = get_invoice_date()
        print()
        # calculate due date and days overdue.
        due_date = invoice_date + timedelta(days = 30)
        current_date = datetime.now()
        days_overdue = (due_date - current_date).days

        # display results
        print('Invoice Date:', invoice_date.strftime(format_str))
        print('Current Date:', current_date.strftime(format_str))
        print('Due Date:    ', due_date.strftime(format_str))

        # Chain condition check
        if days_overdue > 0:
            print('The invoice will due in', days_overdue, 'days')
        else:
            days_due = days_overdue * -1
            print('The invoice is', days_due, 'day(s) overdue. ')

        result = input('Continue?(y/n): ')
        if result == 'n':
            print('Bye...')
            break

if __name__ == '__main__':
    main()
