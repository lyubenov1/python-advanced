from collections import deque

string = deque(input().split())
mid = len(string) // 2
collected = []

main = ('blue', 'yellow', 'red')

secondary = {
    'orange': ('red', 'yellow'),
    'purple': ('red', 'blue'),
    'green': ('yellow', 'blue'),
}

while string:
    left = string.popleft()
    right = string.pop() if string else ''

    result = left + right
    if result in main or result in secondary.keys():
        collected.append(result)
        continue
    result = right + left
    if result in main or result in secondary.keys():
        collected.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        string.insert(len(string) // 2, left)
    if right:
        string.insert(len(string) // 2, right)

result = []

for color in collected:
    if color in main:
        result.append(color)
        continue

    is_collected = True
    for composite in secondary[color]:
        if composite not in collected:
            is_collected = False
            break

    if is_collected:
        result.append(color)

print(result)











