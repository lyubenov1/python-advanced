from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])
count = 0

while count < 5 and chocolates and milk:

    if chocolates and chocolates[-1] <= 0:
        chocolates.pop()
    elif milk and milk[0] <= 0:
        milk.popleft()

    if not chocolates or not milk:
        break

    if chocolates[-1] == milk[0]:
        count += 1
        chocolates.pop()
        milk.popleft()
    else:
        milk.append(milk.popleft())
        if chocolates:
            chocolates[-1] -= 5

    if count >= 5:
        break

if count >= 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print('Chocolate: empty')
if milk:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print('Milk: empty')
