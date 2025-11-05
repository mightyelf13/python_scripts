import sys
def checking():
    a = []
    words = []
    for line in sys.stdin:
        a.append(line.strip().split())
    count = {}
    for i in a:
            words.append(a[i].lower)
            for w in words:
                    if w in count:
                        count[w] += 1
                    else:
                        count[w] = 1
    x = []
    max = 0
    for j in count.values:
         if count.values[j] >= max:
              x.append(count.keys[j])
    print(x)          