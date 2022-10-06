count = 0
track = 0
for i in range(800, 0, -1):
    track += i
    if track + i-1 > 5000:
        count += 1
        track = 0
        continue
count += 1
print(count)
