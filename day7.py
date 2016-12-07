import re


def valid_adress(adress):
    for i in range(0, len(adress)-3):
        sub = adress[i:i+4]
        if sub == sub[::-1] and sub[0] != sub[1]:
            return True
    return False


def find_ssls(adress):
    ssls = []
    for i in range(0, len(adress)-2):
        sub = adress[i:i+3]
        if sub == sub[::-1] and sub[0] != sub[1]:
            ssls += [sub]
    return ssls


def cross_check(supernets, hypernets):
    for x in supernets:
        for y in hypernets:
            if x[1] + x[0] + x[1] == y:
                return True
    return False

with open("day7input.txt", 'r') as puzzle_input:
    data = puzzle_input.readlines()

regx = re.compile("\[.+?\]")
firstcount = 0
secondcount = 0

for line in data:
    hyper_sequences = regx.findall(line)
    for sequence in hyper_sequences:
        line = line.replace(sequence, " ")
    hyper_sequences = list(map(lambda x: x[1:-1], hyper_sequences))
    adresses = line.split(" ")

    adress_ssls = list(reduce(lambda x, y: x + find_ssls(y), adresses, []))
    hyper_ssls = list(reduce(lambda x, y: x + find_ssls(y), hyper_sequences, []))

    if len(adress_ssls) > 0 and len(hyper_ssls) > 0 and cross_check(adress_ssls, hyper_ssls):
            secondcount += 1
    if len(filter(valid_adress, adresses)) > 0 and len(filter(valid_adress, hyper_sequences)) == 0:
        firstcount += 1

print firstcount
print secondcount