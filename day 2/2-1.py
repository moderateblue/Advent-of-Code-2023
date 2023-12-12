f = open("day 2/input.txt", "r")

#12 red
#13 green
#14 blue

test_range = 18

valid = []
not_valid = []

for x in f:
    print(x)
    skip = False

    start_subsets = x.find(":")
    game = int(x[x.find(" "):start_subsets])
    print(game)
    x = x[start_subsets+2:]
    subsets = x.split("; ")
    for i, subset in enumerate(subsets):
        subsets[i] = subset.split(", ")

    for set in subsets:
        if skip == True:
            break
        for cube in set:
            if skip == True:
                break
            if cube.find("red") > -1:
                if int(cube[:cube.find(" ")]) > 12:
                    print("number scraped:", int(cube[:cube.find(" ")]))
                    print("skipped at this set:", set, "this cube:", cube, "this color: red")
                    skip = True
            elif cube.find("green") > -1:
                if int(cube[:cube.find(" ")]) > 13:
                    print("number scraped:", int(cube[:cube.find(" ")]))
                    print("skipped at this set:", set, "this cube:", cube, "this color: green")
                    skip = True
            else:
                if int(cube[:cube.find(" ")]) > 14:
                    print("number scraped:", int(cube[:cube.find(" ")]))
                    print("skipped at this set:", set, "this cube:", cube, "this color: blue")
                    skip = True

    if skip != True:
        valid.append(game)
    else: 
        not_valid.append(game)

    print("subsets: ", subsets)
    print("valid: ", valid)
    #print(sum(valid))

    if skip == True:
        print("not valid")

    print()

    #if test_range <= 0:
    #    break
    #test_range -= 1

f.close()

print(sum(valid))
print(not_valid)