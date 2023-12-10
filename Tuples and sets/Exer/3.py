n = int(input())

result = set()

for _ in range(n):
    current_set = set(input().split())
    result = result.union(current_set)

for el in result:
    print(el)

#n = int(input())
#
#set1 = set()
#
#for i in range(n):
#    set1.update(x for x in input().split())
#
#for el in set1:
#    print(el)