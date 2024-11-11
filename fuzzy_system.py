import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
traffic_density = ctrl.Antecedent(np.arange(0, 301, 1), 'traffic_density')
time_of_day = ctrl.Antecedent(np.arange(6, 21, 1), 'time_of_day')
weather_conditions = ctrl.Antecedent(np.arange(0, 51, 1), 'weather_conditions')
traffic_light_time = ctrl.Consequent(np.arange(1, 61, 1), 'traffic_light_time')

''' Define fuzzy membership functions
'''
traffic_density['low'] = fuzz.trapmf(traffic_density.universe, [0, 0, 100, 100])
traffic_density['mid'] = fuzz.trimf(traffic_density.universe, [50, 125, 200])
traffic_density['high'] = fuzz.trapmf(traffic_density.universe, [150, 300, 300, 300])

time_of_day['morning'] = fuzz.trapmf(time_of_day.universe, [6, 6, 8, 8])
time_of_day['peak_hour_1'] = fuzz.trimf(time_of_day.universe, [7.5, 8.25, 9])
time_of_day['valley_time'] = fuzz.trimf(time_of_day.universe, [8.66, 13, 17.25])
time_of_day['peak_hour_2'] = fuzz.trimf(time_of_day.universe, [17, 18, 19])
time_of_day['night'] = fuzz.trapmf(time_of_day.universe, [18, 18, 20, 20])

weather_conditions['normal'] = fuzz.trapmf(weather_conditions.universe, [0, 0, 10, 10])
weather_conditions['light_rain'] = fuzz.trimf(weather_conditions.universe, [0, 10, 20])
weather_conditions['heavy_rain'] = fuzz.trapmf(weather_conditions.universe, [10, 50, 50, 50])

traffic_light_time['short'] = fuzz.trapmf(traffic_light_time.universe, [1, 1, 20, 20])
traffic_light_time['mid'] = fuzz.trimf(traffic_light_time.universe, [20, 30, 45])
traffic_light_time['long'] = fuzz.trapmf(traffic_light_time.universe, [40, 60, 60, 60])

''' Define control rules
'''
rules = []
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['morning'] & weather_conditions['light'], traffic_light_time['short']))
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['morning'] & weather_conditions['moderate'], traffic_light_time['short']))
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['morning'] & weather_conditions['heavy'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['peak_hour'] & weather_conditions['light'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['peak_hour'] & weather_conditions['moderate'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['peak_hour'] & weather_conditions['heavy'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['valley_time'] & weather_conditions['light'], traffic_light_time['short']))
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['valley_time'] & weather_conditions['moderate'], traffic_light_time['short']))
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['valley_time'] & weather_conditions['heavy'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['night'] & weather_conditions['light'], traffic_light_time['short']))
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['night'] & weather_conditions['moderate'], traffic_light_time['short']))
rules.append(ctrl.Rule(traffic_density['low'] & time_of_day['night'] & weather_conditions['heavy'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['morning'] & weather_conditions['light'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['morning'] & weather_conditions['moderate'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['morning'] & weather_conditions['heavy'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['peak_hour'] & weather_conditions['light'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['peak_hour'] & weather_conditions['moderate'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['peak_hour'] & weather_conditions['heavy'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['valley_time'] & weather_conditions['light'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['valley_time'] & weather_conditions['moderate'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['valley_time'] & weather_conditions['heavy'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['night'] & weather_conditions['light'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['night'] & weather_conditions['moderate'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['medium'] & time_of_day['night'] & weather_conditions['heavy'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['morning'] & weather_conditions['light'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['morning'] & weather_conditions['moderate'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['morning'] & weather_conditions['heavy'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['peak_hour'] & weather_conditions['light'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['peak_hour'] & weather_conditions['moderate'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['peak_hour'] & weather_conditions['heavy'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['valley_time'] & weather_conditions['light'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['valley_time'] & weather_conditions['moderate'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['valley_time'] & weather_conditions['heavy'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['night'] & weather_conditions['light'], traffic_light_time['medium']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['night'] & weather_conditions['moderate'], traffic_light_time['long']))
rules.append(ctrl.Rule(traffic_density['high'] & time_of_day['night'] & weather_conditions['heavy'], traffic_light_time['long']))

# Create the control system based on the rules
control_sys = ctrl.ControlSystem(rules)

# Initialize simulation of the fuzzy system
fuzzy_traffic_light_time_sys = ctrl.ControlSystemSimulation(control_sys)