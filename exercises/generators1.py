def gensqr(n):
    for i in range(1, n):
        yield i**2

for i in gensqr(10):
    print(i)

str1 = 'hello'
s= iter(str1)
print(next(s))
print(next(s))
