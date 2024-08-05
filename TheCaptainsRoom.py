from collections import Counter

n = int(input())
rooms = list(map(int, input()))
a = Counter(rooms) # here Counter keyword helps us in calculating the count of each element

for key in a.keys():
    if a[key] == 1:
        print(key)