def uncompress(part, version):
    uncompressed_length = 0
    part_index = 0
    while part_index < len(part):
        if part[part_index] == '(':
            next_part_index = part_index + 1
            while part[next_part_index] != ')':
                next_part_index += 1
            nstr = part[part_index + 1: next_part_index]
            chars = int(nstr.split("x")[0])
            times = int(nstr.split("x")[1])
            if version == 1:
                uncompressed_length += len(part[next_part_index + 1: next_part_index + chars + 1]) * times
            else:
                uncompressed_length += uncompress(part[next_part_index + 1: next_part_index + chars + 1], 2) * times
            part_index = next_part_index + chars + 1
        else:
            uncompressed_length += 1
            part_index += 1
    return uncompressed_length

with open("day9input.txt") as puzzle_input:
    data = puzzle_input.read().strip()
print uncompress(data, 1)
print uncompress(data, 2)