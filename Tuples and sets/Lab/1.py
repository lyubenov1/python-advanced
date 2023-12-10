numbers_string = input()

occurrences = {}
numbers = [float(x) for x in numbers_string.split(' ')]

for number in numbers:
    if number not in occurrences:
        occurrences[number] = 0
    occurrences[number] += 1

for number, count in occurrences.items():
    print(f'{number:.1f} - {count} times')
