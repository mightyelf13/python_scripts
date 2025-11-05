import sys
#m = []
#for line in sys.stdin:
#    row = []
#    for word in line.split():
#        row.append(word)
#    m.append(row)
#print(m)
def spiral(matrix):
    result = []
    while matrix:
        result += matrix[0]
        if len(matrix) == 1:
            break
        if len(matrix) > 1:
            matrix = list(zip(*matrix[1:]))[::-1]
    print(*result)


m = []
for line in sys.stdin:
    row = []
    for word in line.split():
        row.append(word)
    m.append(row)
spiral(m)
