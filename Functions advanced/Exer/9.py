def palindrome(word, idx):
    if idx >= len(word) // 2
        return True

    left = word[idx]
    right = word[-1 -idx]

    if left != right:
        return False

    return palindrome(word, idx + 1)


print(palindrome("abcba", 0))
