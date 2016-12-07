from collections import Counter
with open("day6input.txt", 'r') as puzzle_input:
    data = puzzle_input.readlines()
pwd = ''
pwd2 = ''
for col in zip(*data):
    pwd += str(Counter(col).most_common()[0][0])
    pwd2 += str(Counter(col).most_common()[-1][0])
print pwd
print pwd2