with open('17-32.txt') as f:
    a = [int(i) for i in f]
    s = 0
    mx = 0
    summ = 0
    count = 0
    for i in a:
        if i % 2 != 0:
            summ+=i
            count += 1
    sredn = summ / count
    for i in range(len(a) - 1):
        if (a[i] % 5 == 0 or a[i+1] % 5 == 0) and (a[i] < round(sredn) or a[i+1] < round(sredn)):
            s += 1;
            mx = max(mx, a[i] + a[i+1])
print(s, mx)
