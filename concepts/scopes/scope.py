
username = "abc"
x = 40

def print_username() :
    print(username)

def get_data() :
    x = 10

    def print_data() :
        print(x)
    
    return print_data

print_data = get_data()
print(print_data())