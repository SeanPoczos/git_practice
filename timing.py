#!/usr/bin/env python3
from timeit import default_timer as timer

start = timer()

a = 0
while a < 1000000:
    a += 1

end = timer()

print(str(end - start) + ' s')




