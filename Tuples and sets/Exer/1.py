n = int(input())
usernames = set()

for _ in range(n):
    usernames.add(input())

for username in usernames:
    print(username)
