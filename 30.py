with open('17-30.txt') as f:
    a = [int(i) for i in f]
    s = 0
    mx = 0
    maxi = 0
    seci = 0
    mini = 0
    for i in range(len(a) - 2):
        maxi = max(a[i], a[i+1], a[i+2])
        mini = min(a[i], a[i+1], a[i+2])
        seci = a[i] + a[i+1] + a[i+2] - maxi - mini
        if maxi**2 == (mini**2 + seci**2):
            s += 1
            mx = max(mx, a[i] + a[i+1] + a[i+2])
print(s, mx)
