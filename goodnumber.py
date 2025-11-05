def isgood(n):
    num = n
    while n> 0:
        d = n % 10
        if d == 0 or num % d != 0:
            return False
        n //= 10
    return True

def goodnums(N):
    count = 0
    for i in range(1, N + 1):
        if isgood(i):
            count += 1
    return count

if __name__ == "__main__":
     N = int(input())
     if N> 0:
       print(goodnums(N))