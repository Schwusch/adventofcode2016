import re
import itertools

def test_all(data):
    data_perm = list(itertools.permutations(data))
    return len(filter(lambda x: (x[0] + x[1]) > x[2], data_perm)) == len(data_perm)

with open("day3input.txt", 'r') as puzzle_input:
    data = puzzle_input.readlines()

data = map(lambda x: map(lambda y: int(y), x), map(lambda x: re.compile('\d+').findall(x), data))
data_filtered = filter(lambda x: test_all(x), data)
data_filtered2 = filter(lambda x: test_all(x), reduce(lambda x, y: x+y, map(lambda x: map(None, *([iter(x)] * 3)), zip(*data))))
print len(data_filtered)
print len(data_filtered2)