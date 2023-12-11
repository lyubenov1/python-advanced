from collections import deque

string = input().split()
nums = deque()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a // b,
    '*': lambda a, b: a * b,
}

for i in string:
    if i in '+-/*':
        while len(nums) > 1:
            left = nums.popleft()
            right = nums.popleft()
            result = operations[i](left, right)
            nums.appendleft(result)
    else:
        nums.append(int(i))

print(nums.popleft())