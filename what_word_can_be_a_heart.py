import func

words = func.get_word_list()

# Pre-compute indices
criteria = [[1, 3], [0, 2, 4], [0, 4], [2]]

# Build optimized indices once
at_pos, has_char = func.optimize_matching(words)

# Use optimized matching
results = [
    word for word in words
    if all(len(func.fast_match(word, words, at_pos, has_char, indices)) > 0 for indices in criteria)
]

with open('results.txt', 'w', encoding='utf-8') as out_file:
    out_file.write('\n'.join(results))

print(results)

