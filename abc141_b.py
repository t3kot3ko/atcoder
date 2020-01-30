import sys
line = sys.stdin.readlines()[0]

if all([c == "R" or c == "U" or c == "D" for c in line[0::2]]) and all([c == "L" or c == "U" or c == "D" for c in line[1::2]]):
    print "Yes"
else:
    print "No"
