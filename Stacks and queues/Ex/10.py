from collections import deque

cups = deque(map(int, input().split(' ')))
bottles = list(map(int, input().split(' ')))
count = 0
wasted = 0

while cups and bottles:
    if cups[0] <= bottles[-1]:
        wasted += abs(bottles.pop() - cups.popleft())
    else:
        cups[0] -= bottles.pop()

if cups:
    cups = [str(item) for item in cups]
    print("Cups: " + " ".join(cups))
elif bottles:
    bottles = [str(item) for item in bottles]
    print("Bottles: " + " ".join(bottles))

print(f"Wasted litters of water: {wasted}")