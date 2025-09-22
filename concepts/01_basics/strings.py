#Strings in python

slogan = "Do or Die"

first_char = slogan[0]
print(first_char)

#slicing
print(slogan[:])
print(slogan[0:4])
print(slogan[:7])
print(slogan[0:])

#Methods
print(slogan.find("Do"))
dir(slogan) #will show all methods that string have and we can use according to use case

words = "He says, \"he is awesome\""
print(words)

path = "\"c:\\app\sec\data\""
print(path)

other_path = r"c:\\sec\data"
print(other_path)