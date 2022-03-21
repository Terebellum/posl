with open('17-24.txt') as f:
    a = [int(i) for i in f]
    s = 0
    mx = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if (a[i] - a[j]) % 45 == 0 and (a[i] % 18 == 0 or a[j] % 18 == 0):
                s += 1
                mx = max(mx, a[i] - a[j])
print(s, mx)
