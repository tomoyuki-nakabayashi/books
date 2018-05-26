s = ""
# ineffective
for substring in substrings:
    s += substring

# more effective
s = "".join(substrings)
