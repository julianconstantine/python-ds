__author__ = 'Julian'

# DISCUSSION QUESTIONS FOR ALGORITHM ANALYSIS
# Give the Big-O performance for each of the following code fragments.
n = 10

# CODE 1:
count1 = 0

for i in range(n):
    for j in range(n):
        k = 2 + 2
        count1 += 1

print(count1)  # Returns 10^2 = 100 for n = 10

# Runs 1 assignment operation in two nested loops, each of which runs n times, for a total of n^2 operations
# Runtime is O(n^2)

# CODE 2:
count2 = 0

for i in range(n):
    k = 2 + 2
    count2 += 1

print(count2)  # Returns 10 for n = 10

# Runs 1 assignment operation in a loop that executes n times, for a total of n operations
# Runtime is O(n)

# CODE 3:
i = n
count3 = 0

while i > 0:
    k = 2 + 2
    count3 += 1

    i //= 2
    count3 += 1

print(count3)  # Returns 2log(16) = 8 for n = 10

# Divides n by 2 until result is less than or equal to 1
# Runs one more assignment operation each time, for a total of 2log(n) operations
# Runtime is O(log(n))

# CODE 4:
count4 = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            k = 2 + 2
            count4 += 1

print(count4)  # Returns 10^3 = 1000 for n = 10

# Runs 1 assignment operation in three nested loops, each of which is run n times
# Runtime is O(n^3)

# CODE 5:
i = n
count5 = 0

while i > 0:
   k = 2 + 2
   count5 += 1

   i //= 2
   count5 += 1

print(count5)  # Returns 2log(16) = 8 for n = 10

# Divides n by 2 until result is less than or equal to 1
# Runs one more assignment operation each time, for a total of 2log(n) operations
# This is the same as code #3
# Runtime is O(log(n))

# CODE 6:
count6 = 0

for i in range(n):
    k = 2 + 2
    count6 += 1
for j in range(n):
    k = 2 + 2
    count6 += 1
for k in range(n):
    k = 2 + 2
    count6 += 1

print(count6)  # Returns 3*10 = 30 for n = 10

# Each loop runs 1 assignment operation n times, for a total of 3n operations
# Runtime is O(n)
