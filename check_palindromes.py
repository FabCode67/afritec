def check_palindromes(strings):
    return [(s, s == s[::-1]) for s in strings]

strings = ["madam", "racecar", "hello", "level", "world"]
result = check_palindromes(strings)
print(result)
