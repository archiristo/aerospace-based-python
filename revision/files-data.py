import numpy as np

planetnames = ["Neptune", "Mercury", "Earth", "Mars", "Venus", "Saturn", "Jupiter", "Uranus"]
gravity = [1.12, 0.38, 1.0, 0.38, 0.91, 0.93, 2.34, 0.92]
tempature = [50, 440, 288, 210, 737, 80, 120, 60 ]

file =  open("planets.txt", "w")
for i in range(len(planetnames)):
    file.write(planetnames[i] + " ")
    file.write("Gravity(g): " +  str(gravity[i]) + " ")
    file.write("Tempature(K): " + str(tempature[i]) + " ")
file.close()

##deneme, orbital detayları
planetnames = ["Neptune", "Mercury", "Earth", "Mars", "Venus", "Saturn", "Jupiter", "Uranus"]
orbitalperiods = [164.8, 0.24, 1.0, 1.88, 0.62, 29.46, 11.86, 84.01]
axialtilts = [28.32, 0.03, 23.44, 25.19, 177.36, 26.73, 3.13, 82.23]

file =  open("orbitals.txt", "w")
for i in range(len(planetnames)):
    file.write(planetnames[i] + " ")
    file.write("Orbital periods: " +  str(orbitalperiods[i]) + " ")
    file.write("Axial tilts: " + str(axialtilts[i]) + " ")
file.close()

#loadtxt
data = np.loadtxt("spacecraft.txt")
data = np.transpose(data)
mass = data[0]
fuel = data[1]
force = data[2]
print(mass)

