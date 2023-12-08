from collections import deque

total = int(input())
queue = deque(int(x) for x in input().split(' '))

print(max(queue))

while len(queue) > 0 and queue[0] <= total:
    total -= queue.popleft()

if len(queue) == 0:
    print('Orders complete')
else:
    orders_left = [str(x) for x in queue]
    print(f"Orders left: {' '.join(orders_left)}")
