## Basic Functions to Data Science
#
## Find out the highest value in an array.
pulse = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
max_value = max(pulse)
print('Maximun value', max_value)

## Find out the lowest value in an array.
min_value = min(pulse)
print('Minimun value:', min_value)

## Get the average value of an array.
import numpy as np

Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]

avg_value = np.mean(Calorie_burnage)
print('Mean value:', avg_value)
