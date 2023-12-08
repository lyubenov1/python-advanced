dd = {'Doncho': 20, 'Ivan': 25, 'Petar': 27}

print(
    sorted(
        dd.items(),
        key=lambda x: x[1],
        reverse=True,
    )
)
