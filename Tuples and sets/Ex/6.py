n = int(input())
set_even = set()
set_odd = set()

for i in range(1, n + 1):
    name = input()
    asci = int(sum([ord(x) for x in name]) / i)

    if asci % 2 == 0:
        set_even.add(asci)
    else:
        set_odd.add(asci)


total_even = sum(set_even)
total_odd = sum(set_odd)

if total_odd == total_even:
    result = set_odd.union(set_even)
elif total_odd > total_even:
    result = set_odd.difference(set_even)
else:
    result = set_odd.symmetric_difference(set_even)

print(*result, sep=', ')
