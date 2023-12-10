n, m = [int(x) for x in input().split()]

set1 = set()
set2 = set()

for i in range(n):
    set1.add(int(input()))

for i in range(m):
    set2.add(int(input()))

print(*set1.intersection(set2), sep='\n')
