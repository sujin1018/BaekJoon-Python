def solution(n, words):
    used = set()
    prev = words[0][0]
    for i, word in enumerate(words):
        if word in used or word[0] != prev:
            return [(i%n)+1, (i//n)+1]
        used.add(word)
        prev=word[-1]
    return [0,0]