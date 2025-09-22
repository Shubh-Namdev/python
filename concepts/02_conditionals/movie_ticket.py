
from datetime import datetime

adult_ticket_price = 12
child_ticket_price = 8
discount_price = 2

user_age = int(input("Enter your age : "))
#day = datetime.now().weekday()
day = 2

if (user_age < 18 and day == 2) :
    print("ticket price : $"+str(child_ticket_price-discount_price))
elif (user_age < 18) :
    print("ticket price : $"+str(child_ticket_price))
elif (day == 2) :
    print("ticket price : $"+str(adult_ticket_price - discount_price))
else :
    print("ticket price : $"+str(adult_ticket_price))


