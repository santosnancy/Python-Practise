num = [[], []]
for lop in range(1, 8):
    num.append(int(input(f'Enter  the {lop}o Number ')))
    for sa, lo in enumerate(num):
        if lo % 2 == 0:
            num[0].append(lop)
        else:
            num[1].append(lop)
print(num)
