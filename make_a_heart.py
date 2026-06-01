import func

word = "loves"

words = func.get_word_list()
at_pos, has_char = func.optimize_matching(words)

result_A = func.fast_match(word, words, at_pos, has_char, [1, 3])
result_B = func.fast_match(word, words, at_pos, has_char, [0, 2, 4])
result_C = func.fast_match(word, words, at_pos, has_char, [0, 4])
result_D = func.fast_match(word, words, at_pos, has_char, [2])

# Check if heart can be made
if not result_A or not result_B or not result_C or not result_D:
    print(f"Cannot make a heart with '{word}'")
else:
    print("Choose 2 words: ")
    print("\n".join(result_A))
    print()
    print("Choose 1 words: ")
    print("\n".join(result_B))
    print()
    print("Choose 1 words: ")
    print("\n".join(result_C))
    print()
    print("Choose 1 words: ")
    print("\n".join(result_D))