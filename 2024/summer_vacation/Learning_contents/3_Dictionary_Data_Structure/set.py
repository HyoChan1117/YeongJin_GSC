
import random

bar = [ random.randint(1, 7) for _ in range(10) ]
print(bar)

foo = set()

for index in range(10):
    foo.add(bar[index])
    
print(foo)