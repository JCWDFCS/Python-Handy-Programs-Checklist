# Class

I have the code:

    class Product:
        def __init__(self,name, price,discount):
            self.name = name
            self.price = price
            self.discount = discount

        def get_discount_amout(self):
            return self.price * self.discount
Create an instance:

    In [2]: book = Product('Think Python', 12.99, 30)
Calculate the discount amount

    In [5]: book.get_discount_amout()
    Out[5]: 389.7
I find the spelling error and arithmetic error,next to correct them in the consoleself.
Firstly I define a correct `get_discount_amount` function.

    def get_discount_amount_correct(self):
        return self.price * self.discount/100
Second to overwrite `book`s previous method.

    book.get_discount_amount = get_discount_amount_correct

Test it.

    In [13]: book.get_discount_amount
    Out[13]: <function __main__.get_discount_amount_correct>
Fatastic...then

    In [14]: book.get_discount_amount()
    TypeError: get_discount_amount_correct() missing 1 required positional argument: 'self'


try,
    In [15]: book.get_discount_amount(self)
    NameError: name 'self' is not defined

alternatively try lambda
    In [16]: book.get_discount_amount = lambda self: self.price * self.discount/100
    TypeError: <lambda>() missing 1 required positional argument: 'self'

In console, object's attributes can be easily overwrite,
How to overwrite its methods?
