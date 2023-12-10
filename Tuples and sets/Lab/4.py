n = int(input())

parking_lot = [input().split(', ') for i in range(n)]
set1 = set()

for command, plate in parking_lot:
    if command == 'IN':
        set1.add(plate)
    else:
        set1.remove(plate)

if set1:
    [print(i) for i in set1]
else:
    print("Parking Lot is Empty")



