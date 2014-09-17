total = 0.0
num = 0
for p in range(60):
    if patients[p, 1] == 0:
        max_count = 0
        for t in range(40):
            if patients[p, t] > max_count:
                max_count = patients[p, t]
        total += max_count
        num += 1
print 'result', total / num
