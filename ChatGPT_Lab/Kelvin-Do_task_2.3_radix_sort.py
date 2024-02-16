import random,time

from random import randint

A=[random.randint(1,1212) for i in range(23)]


length = len(str(max(A)))

print(length) 

rang = 10

print(A)

start=time.time()

for i in range(length):

    B = [[] for k in range(rang)]

for x in A:

    figure =x // (10**i) % 10

    B[figure].append(x)

A = []

for k in range(rang):

    A+=B[k]

end=time.time()

print(end-start)

print(A)