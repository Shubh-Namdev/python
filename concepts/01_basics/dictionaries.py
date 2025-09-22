
#dictionaries in python 
#key value pair

genre_actor = {"action":"Rajni", "suspense_crime":"Ajay", "romance":"Salman", "comedy":"Akshay"}

#access
print(genre_actor["action"])
print(genre_actor.get("comedy"))
for genre in genre_actor :
    print(genre)

for genre in genre_actor :
    print(genre, genre_actor.get(genre))

for key,value in genre_actor.items() :
    print(key, value)

#update
genre_actor["romance"] = "Ranbir"
genre_actor.update("romance")

#dic methods
dir(genre_actor)
genre_actor_copy = genre_actor.copy()
genre_actor.pop("romance")
genre_actor.popitem()
new_dict = {}.fromkeys([1,2,3], 0)
print(new_dict)

#concepts
res = {x:x**2 for x in range(5)}
print(res)

