with open("day 5/test_input.txt", "r") as f:

    seeds_raw = f.readline()
    seeds = seeds_raw[seeds_raw.find(":")+2:].split(" ")
    seeds = [int(x) for x in seeds]
    print(seeds)

