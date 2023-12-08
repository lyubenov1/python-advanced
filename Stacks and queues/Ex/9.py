from collections import deque

price = int(input())
barrel = int(input())
bullets = list(map(int, input().split(' ')))
locks = deque(map(int, input().split(' ')))
intelligence = int(input())
count = 0
condition = False

while bullets:
    bullet = bullets.pop()
    count += 1
    if bullet <= locks[0]:
        lock = locks.popleft()
        print('Bang!')
    elif bullet > locks[0]:
        print('Ping!')

    if count % barrel == 0:
        if bullets:
            print('Reloading!')

    if len(locks) <= 0:
        condition = True
        break

if condition:
    earned = intelligence - (count * price)
    print(f'{len(bullets)} bullets left. Earned ${earned}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")


