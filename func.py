def get_word_list():
    try:
        with open("words.txt", "r") as f:
            words = f.readlines()
        words = [word.strip() for word in words if word.strip()]
        
        if len(words) == 0 :
            return get_word_list_online()
        else:
            return words
    except:
        return get_word_list_online()

def get_word_list_online():
    import requests
    data = requests.get("https://fly.wordfinderapi.com/api/search?length=5&word_sorting=points&group_by_length=true&page_size=10000000&dictionary=wwf2")
    words = list(map(lambda x:x["word"], data.json()["word_pages"][0]["word_list"]))
    with open("words.txt", "w") as f:
        f.write("\n".join(words))
    return words


def match(word, word_list: list[str], indices):
    indices_set = set(indices)
    return [
        candidate for candidate in word_list
        if all(
            (word[i] == candidate[i]) if i in indices_set else (word[i] not in candidate)
            for i in range(5)
        )
    ]


def optimize_matching(words):
    """Pre-build indices for O(1) lookups instead of O(n) scans"""
    # For each position and character, store which words have it at that position
    at_pos = [{} for _ in range(5)]  # words with char at position i
    has_char = [{} for _ in range(5)]  # words containing char anywhere
    
    for word in words:
        for i in range(5):
            char = word[i]
            # Words with this char at this position
            if char not in at_pos[i]:
                at_pos[i][char] = set()
            at_pos[i][char].add(word)
            
            # Words with this char anywhere
            for j in range(5):
                if j != i and word[j] == char:
                    if char not in has_char[i]:
                        has_char[i][char] = set()
                    has_char[i][char].add(word)
    
    return at_pos, has_char


def fast_match(word, words, at_pos, has_char, indices):
    """Use pre-built indices for O(1) lookups instead of O(n) scans"""
    indices_set = set(indices)
    result = set(words)  # Start with all words
    
    for i in range(5):
        char = word[i]
        if i in indices_set:
            # Position must match
            result &= at_pos[i].get(char, set())
        else:
            # Char must NOT appear at this position
            result -= at_pos[i].get(char, set())
    
    return result