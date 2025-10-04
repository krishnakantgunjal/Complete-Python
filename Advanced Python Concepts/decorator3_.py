# Write a decorator timer that calculates how long a function takes to execute.
#  Test it with a function that sums numbers from 1 to 1,000,000.

import time 
def timer(func):
      def wrappper(n):
            start_time = time.time()
            func(n)
            end_time = time.time()
            result = end_time - start_time
            print("total time to excute function :-",result)
      return wrappper
@timer
def Sums(n):
    total=0
    for x in range(0,n+1):
         total += x
    print("sum:-",total)
Sums(1000000)
      