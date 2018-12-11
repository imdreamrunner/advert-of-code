import sys

in_file = sys.argv[1]
in_data = open(in_file, 'r')

arr = [int(a) for a in in_data]

s = 0
hm = set([0])

while True:
    for a in arr:
        s += a
        if s in hm:
            print(s)
            exit(0)
        hm.add(s)
