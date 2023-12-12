f = open("day 3/input.txt", "r")

def solution(test_range = 0):
    arr = []
    number_words = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numbers = []

    lines, chars

    for i, line in enumerate(f):
        arr.append([])
        for j, char in enumerate(line):
            if char != "\n":
                arr[i].append(char)
            chars = j + 1
        lines = i + 1

    counted = [[0 for i in range(chars)] for j in range(lines)]
    
    for row, line in enumerate(arr):
        for col, char in enumerate(line):
            if char == "*":
                around = 0
                nums = []
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        r, c = row + x, col + y
                        if r >= 0 and c >= 0 and r < len(arr) and c < len(arr[r]) and counted[r][c] == 0 and arr[r][c] in number_words:
                            around += 1
                            while c >= 0 and arr[r][c] in number_words:
                                c -= 1
                            c += 1
                            start = c
                            while c < len(arr[r]) and arr[r][c] in number_words:
                                counted[r][c] = 1
                                c += 1
                            j = ""
                            num = j.join(arr[r][start:c])
                            nums.append(int(num))
                if around == 2:
                    numbers.append(nums[0] * nums[1])

    print(sum(numbers))

solution()