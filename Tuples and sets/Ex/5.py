n = int(input())
best_intersection = set()


for _ in range(n):
    first_range, second_range = input().split('-')

    first_start, first_end = [int(x) for x in first_range.split(',')]
    second_start, second_end = [int(x) for x in second_range.split(',')]

    first = set(range(first_start, first_end + 1))
    second = set(range(second_start, second_end + 1))

    current_intersection = first.intersection(second)
    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

print(f'Longest intersection is [{", ".join([str(x) for x in best_intersection])}] with length {len(best_intersection)}')

# ---------------------------------------------------------------------------------------------------

#n = int(input())
#intersections = set()
#
#for i in range(n):
#    first_range, second_range = input().split('-')
#
#    first_start, first_end = [int(x) for x in first_range.split(',')]
#    second_start, second_end = [int(x) for x in second_range.split(',')]
#
#    first_set = frozenset(range(first_start, first_end + 1))
#    second_set = frozenset(range(second_start, second_end + 1))
#
#    intersection1 = first_set.intersection(second_set)
#    intersections.add(intersection1)
#
#longest = max(intersections, key=len)
#print(f'Longest intersection is {list(longest)} with length {len(longest)}')

# ---------------------------------------------------------------------------------------------------

#n = int(input())
#intersections = []
#
#for i in range(n):
#    first_range, second_range = input().split('-')
#
#    first_start, first_end = [int(x) for x in first_range.split(',')]
#    second_start, second_end = [int(x) for x in second_range.split(',')]
#
#    # Ensure that the start of the first range is less than or equal to the start of the second range
#    if first_start > second_start:
#        first_start, second_start = second_start, first_start
#        first_end, second_end = second_end, first_end
#
#    # Check for intersection
#    intersection_start = max(first_start, second_start)
#    intersection_end = min(first_end, second_end)
#
#    if intersection_start <= intersection_end:
#        intersection = list(range(intersection_start, intersection_end + 1))
#        intersections.append(intersection)
#
## Find the longest intersection
#longest = max(intersections, key=len, default=[])
#print(f'Longest intersection is {longest} with length {len(longest)}')
