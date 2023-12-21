string = input().split('|')
result = []

for i in range(len(string) - 1, - 1, - 1):
    result.extend(string[i].strip().split())

print(' '.join(result))
