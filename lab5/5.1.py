values = [10,20,30]
keys = ["ten","twenty","thrity"]

D = dict(zip(keys,values))
x = len(keys)
i = 0
E = {}
for i in range(x):
    E[keys[i]] = values[i]

print(D)
print(E)

F = dict(trzydziesci=30,czterdziesci=40,piecdziestiat=50)

print(F)
G = D.copy()
G.update(F)
print(G)