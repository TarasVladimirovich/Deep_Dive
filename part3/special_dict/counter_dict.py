from collections import defaultdict, Counter
import random
import re

sentence = 'the quick brown fox jumps over the lazy dog'

counter = defaultdict(int)
for c in sentence:
    counter[c] += 1
print(dict(counter))

counter = Counter()
for c in sentence:
    counter[c] += 1
print(counter)
print(Counter(sentence))

print('*' * 25)

c1 = Counter('able was I era I saw elba')
print(c1)
q = (random.randint(0, 10) for _ in range(1_000))
print(type(q))
print(Counter(q))
sentence = '''
his module implements pseudo-random number generators for various distributions.

For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.

On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions. For generating distributions of angles, the von Mises distribution is available.

Almost all module functions depend on the basic function random(), which generates a random float uniformly in the semi-open range [0.0, 1.0). Python uses the Mersenne Twister as the core generator. It produces 53-bit precision floats and has a period of 2**19937-1. The underlying implementation in C is both fast and threadsafe. The Mersenne Twister is one of the most extensively tested random number generators in existence. However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.
'''

words = re.split('\W', sentence)
print(words)
words_count = Counter(words)
print(words_count.most_common(5))
c1 = Counter('abba')
for c in c1.elements():
    print(c)

c1 = Counter()
for i in range(1, 11):
    c1[i] = i
print(list(c1.elements()))

c1 = Counter(a=1, b=2, c=3)
c2 = Counter(b=1, c=2, d=3)
c1.update(c2)
print(c1)
print(c2)
print('*' * 100)
c1 = Counter(a=1, b=2, c=3)
c2 = Counter(a=1, b=2, c=3)

c1.subtract(c2)
print(c1)
c1.subtract(c2)
print(c1)
print('8' * 100)
print('without mutate')
c1 = Counter('aabbcc')
c2 = Counter('abc')
c3 = c1 + c2
c4 = c1 - c2
c5 = c1 & c2
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)

c1 = Counter(a=5, b=1)
c2 = Counter(a=1, b=10)
# minimum a1 b1
print(c1 & c2)
# max a5 b10
print(c1 | c2)
print('*'*100)
c1 = Counter(a=10, b=-10, d=0)
print(+c1)
print(-c1)
