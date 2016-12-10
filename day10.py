def check_robot(roboto):
    if "output" not in roboto and len(robots[roboto]["vals"]) > 1:
        if max(robots[roboto]["vals"]) == 61 and min(robots[roboto]["vals"]) == 17:
            print roboto
        if robots[roboto]["high"] not in robots:
            robots[robots[roboto]["high"]] = {"vals": []}
        if robots[roboto]["low"] not in robots:
            robots[robots[roboto]["low"]] = {"vals": []}
        robots[robots[roboto]["high"]]["vals"] += [max(robots[roboto]["vals"])]
        robots[robots[roboto]["low"]]["vals"] += [min(robots[roboto]["vals"])]
        check_robot(robots[roboto]["high"])
        check_robot(robots[roboto]["low"])

data = open("day10input.txt", "r").readlines()
robots = {}
for line in data:
    parts = line.strip().split(" ")
    if parts[0] == "value":
        if not (parts[-2] + parts[-1]) in robots:
            robots[parts[-2] + parts[-1]] = {"vals": [], "high": "", "low": ""}
        robots[parts[-2] + parts[-1]]["vals"] += [int(parts[1])]
    else:
        if not (parts[0] + parts[1]) in robots:
            robots[parts[0] + parts[1]] = {"vals": [], "high": "", "low": ""}
        robots[parts[0] + parts[1]][parts[3]] = parts[5] + parts[6]
        robots[parts[0] + parts[1]][parts[8]] = parts[-2] + parts[-1]

check_robot(filter(lambda x: len(robots[x]["vals"]) > 1, robots)[0])
print robots["output0"]["vals"][0] * robots["output1"]["vals"][0] * robots["output2"]["vals"][0]
