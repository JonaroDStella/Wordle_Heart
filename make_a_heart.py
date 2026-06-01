import func

word = "loved"

words = func.get_word_list()

result_A = func.match(word, words, [1, 3])
result_B = func.match(word, words, [0, 2, 4])
result_C = func.match(word, words, [0, 4])
result_D = func.match(word, words, [2])

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