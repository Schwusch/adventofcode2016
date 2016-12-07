import re
from collections import Counter


def sort_stuff(x, y):
    if x[1] != y[1]:
        return x[1] - y[1]
    else:
        return ord(y[0]) - ord(x[0])

def decrypt(phrase, id):
    key = int(id[0]) % 26
    translated = ''

    for symbol in phrase[0]:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
            translated += chr(num)
            continue
        else:
            translated += " "
    if "north" in translated:
        print translated
        print id

with open("day4input.txt", 'r') as puzzle_input:
    data = puzzle_input.readlines()

encrypt_name = map(lambda x: re.compile('.+(?=-\d+)').findall(x), data)
sector_id = map(lambda x: re.compile('\d+').findall(x), data)
checksum = map(lambda x: re.compile('(?<=\[).+(?=\])').findall(x), data)

count = 0
for en, secid, cs in zip(encrypt_name, sector_id, checksum):
    test_cs = "".join(map(lambda x: x[0], sorted(Counter(en[0].replace("-", "")).most_common(), cmp=sort_stuff, reverse=True)))[:5]
    if test_cs == cs[0]:
        count += int(secid[0])
        decrypt(en, secid)

print count