##For döngüsü
planets = ["mars", "jupiter", "earth", "moon"]
for planet in planets:
    print(planet)

##While döngüsü
i = 1
while i <= 10:
    print(i)
    i += 1

##If, else if, else döngüleri
num = int(input("Bir sayı yaz: "))

if num < 20:
    print("Sayı 20den küçük")

elif num == 20:
    print("Sayı 20ye eşit")

else:
    print("Sayı 20den büyük")

##Deneme
celestial_objects = {
    "Sirius": 25,
    "Andromeda Galaxy": 1000000,
    "Jupiter": 0.00006,
    "Pleiades": 100,
    "Orion Nebula": 10000


}
#Veriler beraber verilmek istenirse:
for object in celestial_objects.items():
    print(object[0], ":", object[1], "solar units")


#Ayrı verilmek istenirse:
#Sadece isimler
for object in celestial_objects.items():
    print(object[0])

#Sadece sayılar
luminosities = []
for object in celestial_objects.items():
    luminosities.append(object[1])

index = 0
while index < len(luminosities):
    if (luminosities[index] < 200):
        print(luminosities[index])
    index += 1

#break statement
for planet_name in ["Earth", "Mars", "Neptune", "Saturn", "Jupiter"]:
    if planet_name == "Saturn":
        break
    print(planet_name)

#continue statement
for planetname in ["Earth", "Mars", "Neptune", "Saturn", "Jupiter"]:
    if planetname == "Neptune":
        continue
    print(planetname)


#pass statement
for planetinfo in ["Earth", "Mars", "Neptune", "Saturn", "Jupiter"]:
    if planetinfo == "Saturn":
        pass
    elif planetinfo == "Mars":
        print("the red one")
    print(planetinfo)

#deneme-2
mission_duration = 10
fuel_level = 500
distance_to_destination = 500000
mission_time = 0
fuel_consuption_rate = 50
distance_traveled_per_hour = 50000

while mission_time <= mission_duration:
    fuel_level -= fuel_consuption_rate
    distance_to_destination -= distance_traveled_per_hour

    print("Mission time", mission_time)
    print("Remaining fuel", fuel_level)
    print("Remaining road", distance_to_destination)

    if fuel_level == 0 or distance_to_destination == 0:
        break
        
    mission_time += 1
print("Completed")
    
