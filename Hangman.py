import random

list11 = ['I', 'E', 'R', 'L', 'A', 'O', 'T', 'N', 'U', 'C', 'Ț', 'Ă', 'S', 'M', 'D', 'P', 'G', 'B', 'F', 'Ș', 'V', 'Z',
          'H', 'Â', 'Î', 'J', 'K', 'X', 'W', 'Q', 'Y']
f = open("cuvinte.txt", "r+")
trials = 0
lines = open('cuvinte.txt', encoding='utf-8', errors='ignore').read().splitlines()
while lines:
    if not lines:
        break
    else:
        list1 = list11.copy()
        my_line1 = random.choice(lines)
        lines.remove(my_line1)
        my_line = my_line1.split(";")[2]
        attempts = my_line1.split(";")[1]
        my_line = list(my_line)
        attempts = list(attempts)
        x = len(attempts)

        for i in attempts:
            if i in list1:
                list1.remove(i)
        for i in range(1, (len(list1) + 1)):
            k = list1[(i - 1)]
            trials = trials + 1
            for i in range(0, x):
                if my_line[i] == k:
                    attempts[i] = k
                test = 0
                for i in range(0, x):
                    if attempts[i] == '*':
                        test = 1
                if test == 0:
                    break
            if test == 0:
                break
        ok = 0
        for i in range(0, x):
            if attempts[i] != my_line[i]:
                ok = 1
print(trials)
input()
