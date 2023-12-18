i = 1
s = []
with open('sample.txt', 'r') as file:
    for line in file:
        if i % 2 == 0:
            s.append(line)
        i += 1


print(s)