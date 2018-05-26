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