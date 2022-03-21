with open('17-7.txt') as f:
    a = [int(i) for i in f]
    s = 0
    mx = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if (a[i] * a[j]) % 14 != 0:
                s += 1
                mx = max(mx, a[i] + a[j])
print(s, mx)
