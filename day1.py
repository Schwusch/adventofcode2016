NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def poop(pee):
    x = 0
    y = 0
    direction = NORTH
    visited_places = {}
    for instruction in pee:
        newx = x
        newy = y
        if 'R' in instruction:
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1)
            if direction == -1:
                direction = WEST

        if direction == NORTH:
            newy = y + int(instruction[1:])
            for i in range(y + 1, newy + 1):
                try:
                    if visited_places[str(x) + "," + str(i)]:
                        print "Location visited twice. Distance: " + str(abs(x) + abs(i))
                except KeyError:
                    visited_places[str(x) + "," + str(i)] = True
        elif direction == EAST:
            newx = x + int(instruction[1:])
            for i in range(x + 1, newx + 1):
                try:
                    if visited_places[str(i) + "," + str(y)]:
                        print "Location visited twice. Distance: " + str(abs(i) + abs(y))
                except KeyError:
                    visited_places[str(i) + "," + str(y)] = True
        elif direction == SOUTH:
            newy = y - int(instruction[1:])
            for i in range(newy, y):
                try:
                    if visited_places[str(x) + "," + str(i)]:
                        print "Location visited twice. Distance: " + str(abs(x) + abs(i))
                except KeyError:
                    visited_places[str(x) + "," + str(i)] = True
        else:
            newx = x - int(instruction[1:])
            for i in range(newx, x):
                try:
                    if visited_places[str(i) + "," + str(y)]:
                        print "Location visited twice. Distance: " + str(abs(i) + abs(y))
                except KeyError:
                    visited_places[str(i) + "," + str(y)] = True

        y = newy
        x = newx
    return abs(x) + abs(y)

with open("day1input.txt", 'r') as puzzle_input:
    data = puzzle_input.read().split(", ")

poop(data)



