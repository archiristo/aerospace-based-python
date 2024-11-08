travel_time = 8 #hour
speed = 500 #km per hour
fuel_efficiency = 20 #km per liter
name = "a"
surname = "b"

distance = speed * travel_time
fuel_consuption = speed * travel_time / fuel_efficiency
astronaut_fullname = name + " " + surname

print("Astronot adı: " , astronaut_fullname)
print("Gittiği yol: ", distance)
print("Tüketilen yakıt" , fuel_consuption)
