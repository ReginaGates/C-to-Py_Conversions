# Regina Gates
# C-to-Python conversion program
# C program found in the book:
# "C by Dissection Fourth Edition" by Al Kelley and Ira Prohl
# November 12, 2017
# Time code found online at
# https://stackoverflow.com/questions/12444004/how-long-does-my-python-application-take-to-run

# I am finding combination problems take a great deal of time to perform, due to multiple iterations
# in the nested loops. I have recently learned about Big O Notation, and understand some about why that
# happens. This is why I added the timer to the program. Obviously, more calculations take longer to complete.

# This program finds 3 positive integers that add up to a number input by the user.

import time
start_time = time.time()

def addTo(N):
    for i in range(0, N):
        for j in range(0, N):
            for k in range(0, N):
                if i + j + k == N:
                    print("{0} + {1} + {2} = {3}".format(i, j, k, N))
                else:
                    continue

number = input("Please enter a number 1-1000: ")
addTo(number)
print("My program took " + str(time.time() - start_time) + "s to run.")
