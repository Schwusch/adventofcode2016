import numpy
with open("day8input.txt", 'r') as puzzle_input:
    data = puzzle_input.readlines()

display = numpy.zeros((6, 50))
for line in data:
    if "rect" in line:
        cols = int(line.split(" ")[1].split("x")[0])
        rows = int(line.split(" ")[1].split("x")[1][:-1])
        if rows > 0 and cols > 0:
            for i in range(0, rows):
                for j in range(0, cols):
                        display[i][j] = 1
    else:
        which = int(line.split(" ")[2].split("=")[1])
        howmuch = int(line.split(" ")[4])
        if "row" in line:
            display[which] = numpy.roll(display[which], howmuch)
        else:
            rotated = numpy.rot90(display, 3)
            rotated[which] = numpy.roll(rotated[which], -howmuch)
            display = numpy.rot90(rotated)

def conv(a):
    if a > 0:
        return "#"
    else:
        return " "
converted = map(lambda x: reduce(lambda x, y: x + y, map(conv, x)), display)
for line in converted:
    print line
print numpy.sum(display)
print "06.00am is too early :("