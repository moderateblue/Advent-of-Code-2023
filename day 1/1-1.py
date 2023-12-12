f = open("day 1/input.txt", "r")

total = 0

for x in f:
    print(x)
    num = ""
    for char in x:
        if char.isdigit():
            num += char
            break

    for char in reversed(x):
        if char.isdigit():
            num += char
            break
    
    print("num", num)

    total += int(num)

f.close()

print(total)
