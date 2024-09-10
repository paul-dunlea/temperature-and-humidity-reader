import numpy as np #imports numpy as np ( ability for statistics functions)
import matplotlib.pyplot as plt
#imports and uses csv reader function
import csv
with open('sen.csv', 'r') as f:
    readings = list(csv.reader(f, delimiter=';'))
    print(readings[:])
readings = np.genfromtxt("sen.csv", delimiter=",", dtype="float")#assigns a float values as default data types

print('Shape: ', readings.shape)
print('Datatype: ', readings.dtype)
print('Size: ', readings.size)

import matplotlib.pyplot as plt
temp=[]
humidity=[]
for i in range(len(readings)):
    if i%2==0:
        temp.append(readings[i])
    else:
        humidity.append(readings[i])

plt.plot(temp)
plt.title("Temperature Reading")
plt.xlabel("")
plt.ylabel("Temp")
plt.show()
plt.plot(humidity)
plt.title("Humidity Reading")
plt.xlabel("")
plt.ylabel("Humidity")
plt.show()

