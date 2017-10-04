#find the perimeter and area
import math
print('The Area and Perimeter.')
print()
radius = float(input('Please enter a radius: \t\t'))
area = math.pi * radius**2
perimeter = 2 * math.pi * radius
#display the result
print('The area:\t\t %r' %area)
print('The perimeter:\t\t %r' %perimeter)
print()
print('Thanks for using this program.')
