
# Three kinds of mortgages of Fixed, FixedWithPts, TwoRate

def find_payment(loan, r, m):
    """Assumes: loan and r are floats, m an int
        Returns the monthly payment for a mortgage of size
        loan at a monthly rate of r for m months"""
    return loan*(1+r)**m * (r/((1+r)**m-1))

class Mortgage(object):
    """Abstract class for building different kinds of mortgage"""
    def __init__(self, loan, annual_rate, months):
        """Assumes:loan and annual_rate are floats, months an int
            Creates a new mortgage of size loan, duration months,and annual rate annual_rate"""
        # loan**(rate*months) == future value
        # payment
        self.loan = loan
        self.month_rate = annual_rate/12
        self.months = months
        # paid,outstanding, payment
        self.paid = [0]
        self.outstanding = [loan]
        self.payment = find_payment(loan, self.month_rate, months)
        self.legend = None #discription of mortgage
    def make_payment(self):
        """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.month_rate
        self.outstanding.append(self.outstanding[-1] - reduction)
    def get_total_paid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)
    def __str__(self):
        return self.legend

class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + "%"

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100)]
        self.legend = 'Fixed, ' + str(r*100) + '%, ' \
                        + str(pts) + ' points'

class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self.teaser_months = teaser_months
        self.teaser_rate = teaser_rate
        self.next_rate = r/12
        self.legend = str(teaser_rate*100)\
                        + '% for ' + str(self.teaser_months)\
                        + ' months, then ' + str(r*100) + '%'
    def make_payment(self):
        if len(self.paid) == self.teaser_months + 1:
            self.rate = self.next_rate
            self.payment = find_payment(self.outstanding[-1], self.rate, self.months-self.teaser_months)
        Mortgage.make_payment(self) # how does it work?

def compare_mortgages(amt, years, fixed_rate, pts, pts_rate, var_rate1, var_rate2, var_months):
    tot_months = years * 12
    fixed1 = Fixed(amt, fixed_rate, tot_months)
    fixed2 = FixedWithPts(amt, pts_rate, tot_months, pts)
    two_rate = TwoRate(amt, var_rate2, tot_months, var_rate1, var_months)
    morts = [fixed1, fixed2, two_rate]
    for m in range(tot_months):
        for mort in morts:
            mort.make_payment()
    for m in morts:
        print(m)
        print(' Total payment = $' + str(int(m.get_total_paid())))

compare_mortgages(amt=200000, years=10, fixed_rate=0.07, pts=3.25, pts_rate=0.05, var_rate1=0.045, var_rate2=0.095, var_months=12)
