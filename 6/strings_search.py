def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            i -= 1
            k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1


def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    if n < m:
        return -1
    d = 256
    q = 101
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if pattern == text[i:i + m]:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    if n < m:
        return -1
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = pi[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j
    j = 0
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = pi[j - 1]
        if pattern[j] == text[i]:
            j += 1
        if j == m:
            return i - m + 1
    return -1


text = "abracadabra"
pattern = "cad"
print("Boyer-Moore:", boyer_moore(text, pattern))
print("Rabin-Karp:", rabin_karp(text, pattern))
print("Knuth-Morris-Pratt:", kmp(text, pattern))