#The test score Program
print("The Test Scores Program")
print()
print('Enter 3 test scores')
#initialize an accumulator
total_score = 0
for i in range(3):
    score = float(input("Enter test score: "))
    total_score += score
    average_score = total_score / 3

print('The total score: %r' %total_score)
print('The average_score: %r' %average_score)
print('Bye.')
