players = ["Sachin","Dravid","Ganguly","Dhoni","Rohit","Kohli"]
actors = ["Rajini","Kamal","Ajith","Vijay","Prabhu","Trisha"]
fruits = ["Apple","Mango","Pineapple","Jackfruit","Grapes","Pomegranate"]

if "Sachin" in players:
    print("yes he is there")


#list methods

players.append("Pant")
actors.append("Nayan")
fruits.append("Banana")

print(players)
print(actors)
print(fruits)

players.insert(2,"Hardik")
print(players)
players.remove("Hardik")
print(players)
players.pop() # removes the last
print(players)
players.reverse()
print(players)
print(fruits)
print(fruits[-1:])

