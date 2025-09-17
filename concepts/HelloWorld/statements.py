
#if

# temprature = 35
#
# if temprature > 30 :
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temprature > 20 :
#     print("It's a nice day")
# elif temprature > 10 :
#     print("It's a bit cold")
# else :
#     print("colder")


#exercise
user_weight = float(input("Weight : "))
weight_unit = input("(K)g or (L)bs : ").lower()

weight = 0.0
if weight_unit == "l" :
    weight = user_weight / 2.40
    print("Weight in Kg : "+str(round(weight,2)))
elif weight_unit == "k" :
    weight = user_weight * 2.40
    print("Weight in Lbs : " + str(round(weight,2)))
else:
    print("please enter either L/l or K/k")

