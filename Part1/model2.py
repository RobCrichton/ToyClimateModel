# model
import numpy as np
import matplotlib.pyplot as plt
import time

t = 0
temperature_planet = 200
temperature_atmosphere = 250

epsilon = 0.25
dt = 60 * 10
heat_capacity = 1E5
insolation = 1370
sigma = 5.67E-8
planet_radius = 6.4E6

def AreaOfACircle(radius):
     return np.pi * radius ** 2

def SurfaceAreaOfASphere(radius):
     return 4 * np.pi * radius ** 2

def StefanBoltzmann(temperature):
     return sigma * temperature ** 4

planet_disc_area = AreaOfACircle(planet_radius)
planet_sphere_area = SurfaceAreaOfASphere(planet_radius)

plt.scatter(y = temperature_planet, x = t, \
          s = 2, \
          color = 'blue')
plt.ion()
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.show()

while True:
     temperature_planet += \
          dt \
          * (planet_disc_area * insolation - planet_sphere_area * StefanBoltzmann(temperature_planet)) \
          / (heat_capacity * planet_sphere_area)
     t += dt
     plt.scatter( \
          y = temperature_planet, \
          x = t, \
          s = 2, \
          color = 'blue')
     plt.pause(0.001)
     time.sleep(0.001)

 
