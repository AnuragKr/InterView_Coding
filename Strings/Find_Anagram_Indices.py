from collections import Counter,defaultdict


def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)


def anagram_indices_naive(word, s):
    result = []
    for i in range(len(s) - len(word) + 1):
        window = s[i:i+len(word)]
        if is_anagram(window, word):
            result.append(i)
    return result

#Faster Solution
def del_if_zero(dict,char):
    if dict[char] == 0:
        del dict[char]

def anagram_indices(word,s):
    result = []

    freq = defaultdict(int)
    for char in word:
        freq[char] += 1

    for char in s[:len(word)]:
        freq[char] -= 1
        del_if_zero(freq,char)
    
    if not freq:
        result.append(0)

    for i in range(len(word),len(s)):
        start_char,end_char = s[i - len(word)],s[i]
        freq[start_char] += 1
        del_if_zero(freq,start_char)

        freq[end_char] -= 1
        del_if_zero(freq,)


if __name__ == "__main__":
    word = 'ab'
    s = 'abxaba'
    print(anagram_indices(word, s))
