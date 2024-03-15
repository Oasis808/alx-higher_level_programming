#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is positive".format(number))
elif number == 0:
    print("{:d} is zero".format(number))
else:
<<<<<<< HEAD
    print("{:d} is negative".format(number))
=======
    print("{:d} is zero".format(number))
>>>>>>> 828075f6f7c09cb4a149b58d2d395261b3736400
