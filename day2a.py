import sys

in_file = sys.argv[1]
in_data = open(in_file, 'r')

def count_char(word):
    hm = {}
    for c in word:
        if c not in hm:
            hm[c] = 1
        else:
            hm[c] += 1
    return hm.values()

c2 = 0
c3 = 0

for word in in_data:
    counts = count_char(word)
    if 2 in counts:
        c2 += 1
    elif 3 in counts:
        c3 += 1

print(c2 *  c3)
