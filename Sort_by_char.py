def sort_strings_by_last_char(strings):
    return sorted(strings, key=lambda s: s[-1])

strings1 = ('cat', 'dog', 'elk', 'mouse', 'shark', 'wolf')
result = sort_strings_by_last_char(strings1)
print(result)