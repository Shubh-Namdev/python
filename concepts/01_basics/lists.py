
sports_equip = ["football", "shuttle", "bat", "badminton"]

print(sports_equip[0])
print(sports_equip[-1])

#slicing
sel_sports_equip = sports_equip[2:]
print(sel_sports_equip)
badminton_equip = [sports_equip[1], sports_equip[3]]
print(badminton_equip)

#list methods
dir(sports_equip) #shows all list methods
sports_equip.append("ball")
print(sports_equip)
sports_equip.insert(3, "ball")

#iterate
for equip in sports_equip :
    print(equip)

if 'ball' in sports_equip :
    print("yes, i have")


#some concepts
res = [x**2 for x in range(10)]
print(res)


