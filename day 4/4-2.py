with open("day 4/input.txt") as f:

    counts = [1 for i in range(len(f.readlines()))]
    f.seek(0)

    for index, line in enumerate(f):
        #print(line)
        line = line.replace("  ", " ")
        winning = line[line.find(":") + 2:line.find("|") - 1].split(" ")
        winning = [int(i) for i in winning]
        my_nums = line[line.find("|") + 2:line.find("\n")].split(" ")
        my_nums = [int(i) for i in my_nums]

        wins = 0
        
        for i in my_nums:
            if i in winning:
                wins += 1
        
        #print("matches: ", wins)
        
        for copies in range(counts[index]):
            for i in range(1, wins + 1):
                counts[index + i] += 1
        
        #print(counts)

print(sum(counts))