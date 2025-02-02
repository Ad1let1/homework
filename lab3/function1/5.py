s = input()

def permut(s):
    def permute(prefix, remaining):
        if len(remaining) == 0:
            print(prefix)
        else:
            for i in range(len(remaining)):
                permute(prefix + remaining[i], remaining[:i] + remaining[i+1:])
    permute("", s)

permut(s)