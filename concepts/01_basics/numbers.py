from decimal import Decimal
from random import random

#standard rules
marks = 10.4
bonus = 10.12
discipline = 20
behaviour  = 10

#not recommened
total = marks + bonus * discipline * behaviour
total = discipline,behaviour #return a tuple

# recommended and clear
total = (marks + bonus) * (discipline * behaviour)
total = (marks + bonus) * (float(discipline) * float(behaviour))

#some inner issues in python
result = (0.1 + 0.1 + 0.1) - 0.3 #returns unexpected values
result = (Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) - Decimal('0.3') #fix import required lib

#octal/hexa/binary
octNumber = 0o100
hexaNumber = 0x100
binNumber = 0b100

octalNum = oct(100)
hexNum = hex(100)
binNum = bin(100)

octalNum = int('100', 8)
hexdecNum = int('100', 16)
binaryNum = int('100', 2)

#import libs
dir('imported lib name')

#sets
#an empty set has value - set()
setOne = {1,2,3}
setTwo = {1,3}

resultSet = setOne & setTwo #intersection
resultSet = setOne | setTwo #union
resultSet = setOne - {1,2,3} #returns set()

#list
numbers = [1,2,4,3]
dir(numbers) #use methods as per use case

number = numbers[1:3] # return a new list



