
fruit_status = {"green":"Unripe", "yellow":"Ripe", "brown":"Overripe"}

user_input = str(input("Enter your fruit color : ")).lower()

print(fruit_status.get(user_input))