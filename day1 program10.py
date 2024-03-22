def modify_string(S):
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    freq = {}
    for char in S:
        freq[char] = freq.get(char, 0) + 1

    for char in S:
        index = (alphabet.index(char) + freq[char]) % 26  
        result += alphabet[index]

    return result

S = "ghee"
print(modify_string(S))  
