def is_vip(guest):
    return guest[0].isdigit()

n = int(input())

vip = set()
non_vip = set()

for _ in range(n):
    reservation = input()
    if is_vip(reservation):
        vip.add(reservation)
    else:
        non_vip.add(reservation)

while True:
    guest = input()
    if guest == 'END':
        break

    if is_vip(guest):
        vip.remove(guest)
    else:
        non_vip.remove(guest)

print(len(vip) + len(non_vip))
[print(guest) for guest in sorted(vip)]
[print(guest) for guest in sorted(non_vip)]
