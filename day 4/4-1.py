f = open("day 4/input.txt")

def solution():
    total_points = []

    for line in f:
        line = line.replace("  ", " ")
        winning = line[line.find(":") + 2:line.find("|") - 1].split(" ")
        winning = [int(i) for i in winning]
        my_nums = line[line.find("|") + 2:line.find("\n")].split(" ")
        my_nums = [int(i) for i in my_nums]

        count = 0
        points = 0
        
        for i in my_nums:
            if i in winning:
                count += 1
        
        if count >= 1:
            points = 1
            count -= 1
        
        points = points << count
        total_points.append(points)
    
    print(sum(total_points))



solution()