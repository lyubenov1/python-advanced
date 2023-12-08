def words_sorting(*args):
    result = {}

    for key in args:
        result[key] = sum(ord(ch) for ch in key)

    total_values = sum(result.values())
    if total_values % 2 == 0:
        laina = sorted(result.items())
    else:
        laina = sorted(result.items(), key=lambda x: x[1], reverse=True)

    return '\n'.join(f'{word} - {count}' for (word, count) in laina)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

