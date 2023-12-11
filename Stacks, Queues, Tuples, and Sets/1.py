first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

n = int(input())

for i in range(n):
    command = input().split()
    if len(command) == 2:

        if first.issubset(second) or second.issubset(first):
            print('True')
        else:
            print('False')

    else:
        operation = command[0]
        number = command[1]
        numbers = set(map(int, command[2:]))

        if operation == 'Add':
            if number == 'First':
                first.update(numbers)
            elif number == 'Second':
                second.update(numbers)

        elif operation == 'Remove':
            if number == 'First':
                first.difference_update(numbers)
            elif number == 'Second':
                second.difference_update(numbers)

print(*first, sep=', ')
print(*second, sep=', ')
