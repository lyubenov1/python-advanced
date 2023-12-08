def kwargs_length(**kwargs):
    return len(kwargs)


dict = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dict))
