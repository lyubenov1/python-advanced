original_string = input()

s = []
for character in original_string:
    s.append(character)

reversed_string = ''

while s:
    reversed_string += s.pop()
# reversed_string += s.pop()   # pop the top element

print(reversed_string)
