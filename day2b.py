import sys

in_file = sys.argv[1]
in_data = open(in_file, 'r')

hs = set()

for word in in_data:
    word = word.strip()
    for i in range(0, len(word)):
        subword = str(i) + ":" + word[0:i] + word[i+1:]
        if subword in hs:
            print(subword.split(":")[1])
            exit(0)
        hs.add(subword)
