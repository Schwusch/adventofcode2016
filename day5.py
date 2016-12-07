import hashlib


def one():
    indexx = 0
    pwrd = ''
    while len(pwrd) != 8:
        seed = "wtnhxymk" + str(indexx)
        md5hash = hashlib.md5(seed).hexdigest()
        if md5hash.startswith("00000"):
            pwrd += md5hash[5]
        indexx += 1

    print "pwd: " + pwrd


def two():
    index = 0
    pwd = ['X'] * 8
    counter = 0
    while counter != 8:
        md5hash = hashlib.md5("wtnhxymk" + str(index)).hexdigest()
        if md5hash.startswith("00000") and not md5hash[5].isalpha() and int(md5hash[5]) < 8 and pwd[int(md5hash[5])] == 'X':
            pwd[int(md5hash[5])] = md5hash[6]
            print "".join(pwd)
            counter += 1
        index += 1

two()