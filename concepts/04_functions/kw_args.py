def print_full_name(**kwargs) :
    for key,value in kwargs.items() :
        print(value)

print_full_name(first_name="Joe", last_name="Root")
print_full_name(last_name="Root", first_name="Joe")
print_full_name(last_name="Root", first_name="Joe", address="England")