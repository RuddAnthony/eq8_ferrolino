import time

x = 0
y = 0

up = 1
n = int(input("Input a number (10, 100, 1,000, 10,000, 100,000): "))

def for_loop_function(x, n):
    time_start = time.time()
    for i in range(n):
        x += i
        time_end = time.time()
    time_total = time_end - time_start

    print("The sum from 1 to", n, "is:",x)
    print("For-Loop Execution Time:",time_total)
        
    
def while_loop_function(up, y, n):
    time_start = time.time()
    while up < n:
        y += up
        up += 1
        time_end = time.time()
    time_total = time_end - time_start
    
    print("The sum from 1 to", n, "is:",y)
    print("While-Loop Execution Time:",time_total)

loop_for = for_loop_function(x, n)

loop_while = while_loop_function(up, y, n)
