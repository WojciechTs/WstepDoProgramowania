X = list(range(10))
print(X)
X[:0] = X[-3:]
print(X)
del X[-3:]
print(X)