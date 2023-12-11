f = open("day 1/input.txt", "r")

total = 0

spelled = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
spelled_match = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0

#test_range = 10

for x in f:
    count += 1
    print(x)
    num = ""
    words = {}
    for word in spelled:
        if x.find(word) > -1:
            words[x.find(word)] = word
        if x.rfind(word) > -1:
            words[x.rfind(word)] = word

    for index, char in enumerate(x):
        if char.isdigit():
            print("char: ", char)
            words[index] = spelled[int(char) - 1]
            print("words[index]: ", index, ": ", words[index])
            break

    for index, char in enumerate(reversed(x)):
        if char.isdigit():
            real_index = len(x) - index - 1
            print("char: ", char)
            words[real_index] = spelled[int(char) - 1]
            print("words[index]: ", real_index, ": ", words[real_index])
            break

    print(words)
    min_num_spelled = words[min(words)]
    max_num_spelled = words[max(words)]

    num += str(spelled_match[spelled.index(min_num_spelled)])
    num += str(spelled_match[spelled.index(max_num_spelled)])

    total += int(num)

    print("first: ", min_num_spelled)
    print("last: ", max_num_spelled)
    print("num: ", num)
    print("total", total)

    #if test_range <= 0:
    #    break
    #test_range -= 1

f.close()

print(total)
print(count)