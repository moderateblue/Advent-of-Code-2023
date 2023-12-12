f = open("day 2/input.txt", "r")

#12 red
#13 green
#14 blue

test_range = 18

min_powers = []

for game_line in f:
    line_dict = {}
    game_line = game_line[game_line.find(":") + 2:game_line.find("\n")]
    print("game_line:", game_line)
    subsets = game_line.split("; ")
    print("subsets:", subsets)
    for i, subset in enumerate(subsets):
        subsets[i] = subset.split(", ")
        for cube in subsets[i]:
            print("cube:", cube)
            num, color = cube.split(" ")
            num = int(num)
            print(num, color)
            if color in line_dict:
                if num > line_dict[color]:
                    line_dict[color] = num
                    print("changed", color, "to", num)
            else:
                line_dict[color] = num
                print("added", color, "with num", num)
    
    min_powers.append(line_dict["red"] * line_dict["blue"] * line_dict["green"])
    print(line_dict["red"] * line_dict["blue"] * line_dict["green"])

    #if test_range <= 0:
    #    break
    #test_range -= 1

print(sum(min_powers))


f.close()