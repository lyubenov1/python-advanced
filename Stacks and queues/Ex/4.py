string = [int(x) for x in input().split(' ')]
rack = int(input())
count = 0
rack_count = 1

while string:
    count += string.pop()
    if count >= rack:
        count = abs(count - rack)
        rack_count += 1
    elif count > 0 and sum(string) < rack:
        if len(string) == 0:
            rack_count += 1

print(rack_count)