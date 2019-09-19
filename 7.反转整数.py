def reverse(x):
    flag = 1 if x>=0 else -1
    x = abs(x)
    res = 0
    while(x):
        tmp = res*10 + x%10
        res = tmp
        x = x // 10
    res = flag*res
    if -2 ** 31 <= res <= 2**31 -1:
        return res
    else:
        return 0
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
#    val = map(int, line.split())
    n = int(line)
    print reverse(n)
