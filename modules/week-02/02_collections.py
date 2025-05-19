#List 
movies= ["Big Fish", "Princess Bride", " The Grannd Budapest Hotel"]
print(movies)
#Append
movies.append("The Matrix")
print(movies)
#Remove
movies.remove("Big Fish")
print(movies)
#Insert
movies.insert(1, "Big Fish")
print(movies)

#tuple cant be changed
bdays = (15, 28, 10, 8)
print(bdays[2])

# Dictionarys can be changed

people = [
    {"name": "Jeff", "age": 33, "hobby": "coding"},
    {"name": "Jeongwon", "age": 32, "hobby": "singing"},
    {"name": "Domenick", "age": 30, "hobby": "teaching"},
]
#print Jeongwon's age
print(people[1]["age"])

#add a new person
people.append({"name": "Raymond", "age": 12, "hobby": "pokemon"})
print(people)

#Remove Jeff
del people[0]

print(people)