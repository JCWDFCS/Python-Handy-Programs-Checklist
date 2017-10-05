
#水电费计算app
print('水电缴费分账单')

total_amount = float(input('总金额： \t'))
total_persons = float(input('总人数： \t'))

fees_of_one = round(total_amount / total_persons, 2)
fees_of_two = round(total_amount / total_persons * 2, 2)

#Display
print('单人费用： \t' + str(fees_of_one))
print('两人费用： \t' + str(fees_of_two))
