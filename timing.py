#!/usr/bin/env python3
from timeit import default_timer as timer
import random

start = timer()

a = 0
while a < random.randint(1000000, 10000000000000):
    a += 1

end = timer()

print(str(end - start) + ' s')




