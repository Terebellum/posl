with open('17-26.txt') as f:
    a = [int(i) for i in f]
    s = 0
    mx = 0
    for i in range(len(a) - 1):
        if (a[i] + a[i+1]) % 5 == 0 and (a[i] % 3 == 0 or a[i+1] % 3 == 0):
            s += 1;
            mx = max(mx, a[i] + a[i+1])
print(s, mx)
