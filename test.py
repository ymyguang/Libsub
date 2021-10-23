l = []
for seat in range(0, 100):
    if 48 <= seat <= 77 or 1 <= seat <= 38:
        l.append(seat)  # 座位号

index = len(l) * 0.64
index = int(index)
print(l)
print(l[index])
