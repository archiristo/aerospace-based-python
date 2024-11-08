thrust = float(input("enter the thrust: "))
massflow_rate = float(input("enter the mass flow rate: "))
spesific_impulse = thrust / (massflow_rate * 9.81)
exhaust_velocity = spesific_impulse * 9.81

print("Spesific impulse is equal to: ",str(spesific_impulse))
print("Exhaust velocity is equal to: ",str(exhaust_velocity))