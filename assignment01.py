#Sum of all the multiples of 3 or 5 below 1000

number = 1000

i = 1

sum = 0

for i in range (number):
           if (i % 3 == 0) | (i % 5 == 0):
               sum += i

print(sum)



