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
rules.append(ctrl.Rule(room_temperature['low'] & relative_humidity['low'], output_voltage['low']))
rules.append(ctrl.Rule(room_temperature['low'] & relative_humidity['medium'], output_voltage['mid_low']))
rules.append(ctrl.Rule(room_temperature['low'] & relative_humidity['high'], output_voltage['mid_high']))
rules.append(ctrl.Rule(room_temperature['medium'] & relative_humidity['low'], output_voltage['low']))
rules.append(ctrl.Rule(room_temperature['medium'] & relative_humidity['medium'], output_voltage['medium']))
rules.append(ctrl.Rule(room_temperature['medium'] & relative_humidity['high'], output_voltage['high']))
rules.append(ctrl.Rule(room_temperature['high'] & relative_humidity['low'], output_voltage['mid_low']))
rules.append(ctrl.Rule(room_temperature['high'] & relative_humidity['medium'], output_voltage['mid_high']))
rules.append(ctrl.Rule(room_temperature['high'] & relative_humidity['high'], output_voltage['high']))

# Create the control system based on the rules
control_sys = ctrl.ControlSystem(rules)

# Initialize simulation of the fuzzy system
fuzzy_air_conditioning_sys = ctrl.ControlSystemSimulation(control_sys)

# Input the initial values
fuzzy_air_conditioning_sys.input['room_temperature'] = 25
fuzzy_air_conditioning_sys.input['relative_humidity'] = 73

# Get the fuzzy membership of the values
fuzzy_air_conditioning_sys.compute()

# Calculate result
result_voltage = fuzzy_air_conditioning_sys.output['output_voltage']
print("Resulting applied voltage:", result_voltage, "V")

# Plot the inputs and output
room_temperature.view(sim=fuzzy_air_conditioning_sys)
plt.title("Room Temperature (°C)")
relative_humidity.view(sim=fuzzy_air_conditioning_sys)
plt.title("Relative Humidity (%)")
output_voltage.view(sim=fuzzy_air_conditioning_sys)
plt.title("Output Voltage (V)")
plt.show(block=True)