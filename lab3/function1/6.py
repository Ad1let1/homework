def reverse_sentence(s):
    a = s.split()
    b = reversed(a)
    s2 = ' '.join(b)
    return s2
s = "We are ready"
print(reverse_sentence(s))