number = int(input())
parking_lot = set()

parking_lot_logs = [input() for _ in range(number)]

for car in parking_lot_logs:
    direction, car_number = car.split(', ')
    if direction == 'IN':
        parking_lot.add(car_number)
    elif direction == 'OUT':
        parking_lot.remove(car_number)

if parking_lot:
    [print(car_number) for car_number in parking_lot]
else:
    print('Parking Lot is Empty')
