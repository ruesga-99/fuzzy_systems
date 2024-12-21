import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define fuzzy variables
room_temperature = ctrl.Antecedent(np.arange(20, 41, 1), 'room_temperature')
relative_humidity = ctrl.Antecedent(np.arange(70, 91, 1), 'relative_humidity')
output_voltage = ctrl.Consequent(np.arange(0, 13, 1), 'output_voltage')

''' Define fuzzy membership functions
'''
room_temperature['low'] = fuzz.trapmf(room_temperature.universe, [20, 20, 20, 30])
room_temperature['medium'] = fuzz.trimf(room_temperature.universe, [20, 30, 40])
room_temperature['high'] = fuzz.trapmf(room_temperature.universe, [30, 40, 40, 40])

relative_humidity['low'] = fuzz.trapmf(relative_humidity.universe, [70, 70, 70, 80])
relative_humidity['medium'] = fuzz.trimf(relative_humidity.universe, [70, 80, 90])
relative_humidity['high'] = fuzz.trapmf(relative_humidity.universe, [80, 90, 90, 90])

output_voltage['low'] = fuzz.trapmf(output_voltage.universe, [0, 0, 0, 3])
output_voltage['mid_low'] = fuzz.trimf(output_voltage.universe, [0, 3, 6])
output_voltage['medium'] = fuzz.trimf(output_voltage.universe, [3, 6, 9])
output_voltage['mid_high'] = fuzz.trimf(output_voltage.universe, [6, 9, 12])
output_voltage['high'] = fuzz.trapmf(output_voltage.universe, [9, 12, 12, 12])

''' Define control rules
'''
rules = []
