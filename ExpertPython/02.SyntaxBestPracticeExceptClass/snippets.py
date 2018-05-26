'''
Concat strings.
'''
s = ""
# ineffective
for substring in substrings:
    s += substring

# more effective
s = "".join(substrings)

'''
List comprehension
'''

# ugly
evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)

# Elegant
[i for i in range(10) if i % 2 == 0]

'''
Other idioms
'''

i = 0
for element in ['one', 'two', 'three']:
    print(i, element)
    i += 1

# enumerate
for i, element in enumerate(['one', 'two', 'three']):
    print(i, element)

# zip
for item in zip(*zip([1, 2, 3], [4, 5, 6])):
    print(item)

# unpack
first, second, *rest = 0, 1, 2, 3
first, *inner, last = 0, 1, 2, 3
(a, b), (c, d) = (1, 2), (3, 4)