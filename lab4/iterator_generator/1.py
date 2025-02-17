def gen(N):
    for i in range(1, N+1):
        yield(i*i)
N = int(input())
for i in gen(N):
    print(i)