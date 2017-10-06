# anual value is to invest at the end of the year.

def calculate_future_value(monthly_investment, yearly_interest_rate, years=20):
    #convert the yearly values to monthly values.
    print('Entering calculate_future_value():')
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12
    #calculate future value,initialize the future value.
    future_value = 0.0
    for i in range(0, months):
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_investment
        future_value += monthly_interest_amount
        # start at the end of the year. start with 'i+1'
        print('month = ', i+1,'future value = ',round(future_value,2))
        if i % 12 == 0:
            print('year =', i+1/12, 'future value = ', round(future_value,2))
    return future_value


def find_payment(loan, r, m):
    """Assumes: loan and r are floats, m an int
        Returns the monthly payment for a mortgage of size
        loan at a monthly rate of r for m months"""
    return loan*(1+r)**m * (r/((1+r)**m-1))

class Mortgage(object):
    """Abstract class for building different kinds of mortgage"""
    def __init__(self, loan, annRate, months):
        """Assumes:loan and annRate are floats, months an int
            Creates a new mortgage of size loan, duration months,and annual rate annRate"""
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0]
        self.outstanding = [loan]
        self.payment = find_payment(loan, self.rate, months)
        self.legend = None #discription of mortgage
    def makePayment(self):
        """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)
    def get_total_paid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)
    def __str__(self):
        return self.legend


def main():
    choice = 'y'
    while choice.lower() == 'y':
        monthly_investment = float(input('Enter monthly investment:\t'))
        yearly_interest_rate = float(input('Enter yearly interest rate:\t'))
        years = int(input('Enter number of years: \t\t'))

        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years)
        print('Future value:\t\t\t' + str(round(future_value, 2)))
        print()

        choice = input("Continue? (y/n): ")
    print('Bye!')

if __name__ == "__main__":
     main()
