
def numbers_sum(*args) :
    print(args)
    for num in args :
        print(num)
    #return sum(args)

print(numbers_sum(1,2))
print(numbers_sum(1,2,3,4))
print(numbers_sum(1,2,3,5,8,9))