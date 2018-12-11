import sys

in_file = sys.argv[1]
in_data = open(in_file, 'r')

arr = [int(a) for a in in_data]

print(sum(arr))
