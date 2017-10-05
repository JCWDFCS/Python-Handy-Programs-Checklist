#The invoice Program
#Get the customer's entries
customer_type = input('Enter the customer type (r/w):\t')
invoice_total = int(input('Enter the total invoice:\t'))
print()
# check the value for discount_percent 'r'for retail, 'w' for wholesale,
if customer_type.lower() == 'r':
    if invoice_total > 0 and invoice_total < 100:
        discount_percent = 0
    elif invoice_total >= 100 and invoice_total < 250:
        discount_percent = 0.1
    elif invoice_total >= 250 and invoice_total < 500:
        discount_percent = 0.2
    elif invoice_total >= 500:
        discount_percent = 0.25

elif customer_type.lower() == 'w':
    if invoice_total > 0 and invoice_total < 500:
        invoice_total = 0.4
    elif invoice_total >= 500:
        invoice_total = 0.5
#set discount to zero if neither Retail or wholesale.
else:
    discount_percent = 0
#calculate
discount_amount = invoice_total * discount_percent
new_invoice_total = invoice_total * (1-discount_percent)
#display
print('Invoice total: \t\t\t' + str(invoice_total))
print('Discount percent: \t\t' + str(discount_percent))
print('Discount amount: \t\t' +str(discount_amount))
print('New invoice total: \t\t' + str(new_invoice_total))
print()
print('Bye')
