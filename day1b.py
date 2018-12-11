import sys

in_file = sys.argv[1]
in_data = open(in_file, 'r')

arr = [int(a) for a in in_data]

s = 0
hs = set([0])

while True:
    for a in arr:
        s += a
        if s in hs:
            print(s)
            exit(0)
        hs.add(s)
