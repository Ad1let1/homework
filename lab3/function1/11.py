def check(s):
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
s = input()
print(check(s))