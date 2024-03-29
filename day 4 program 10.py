def isScramble(s1, s2):
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False

    n = len(s1)
    for i in range(1, n):
        if (isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])) or \
           (isScramble(s1[:i], s2[n-i:]) and isScramble(s1[i:], s2[:n-i])):
            return True

    return False


s1 = "great"
s2 = "rgeat"
print(isScramble(s1, s2))  
