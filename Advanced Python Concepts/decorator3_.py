# Write a decorator timer that calculates how long a function takes to execute.
#  Test it with a function that sums numbers from 1 to 1,000,000.

import time 
def timer(func):
      def wrappper():
            start_time = time.time()
            func()
            end_time = time.time()
            result = end_time - start_time
            print("total time to excute function :-",result)
      return wrappper
@timer
def Sums():
    total=0
    for x in range(0,1000001):
         total += x
         print("sum:-",total)
Sums()
      