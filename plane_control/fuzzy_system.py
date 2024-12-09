import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define fuzzy variables
velocity = ctrl.Antecedent(np.arange(0, 1001, 1), 'velocity')
angle = ctrl.Antecedent(np.arange(-10, 11, 1), 'angle')
position = ctrl.Antecedent(np.arange(0, 11, 1), 'position')

''' Define fuzzy membership functions
'''
velocity['low'] = fuzz.trapmf(velocity.universe, [0, 0, 450, 500])
velocity['ok'] = fuzz.trimf(velocity.universe, [450, 550, 700])
velocity['high'] = fuzz.trapmf(velocity.universe, [550, 850, 1000, 1000])

angle['down'] = fuzz.trapmf(angle.universe, [-10, -10, -5, 0])
angle['level'] = fuzz.trimf(angle.universe, [-5, 0, 5])
angle['up'] = fuzz.trapmf(angle.universe, [0, 5, 10, 10])

position['low'] = fuzz.trapmf(position.universe, [0, 0, 0, 4])
position['low_med'] = fuzz.trimf(position.universe, [2, 4, 6])
position['med'] = fuzz.trimf(position.universe, [4, 6, 8])
position['high_med'] = fuzz.trimf(position.universe, [6, 8, 10])
position['high'] = fuzz.trapmf(position.universe, [8, 10, 10, 10])

''' Define control rules
'''
rules = []

# Create the control system based on the rules
control_sys = ctrl.ControlSystem(rules)

# Initialize simulation of the fuzzy system
fuzzy_plane_control_sys = ctrl.ControlSystemSimulation(control_sys)

# Plot the inputs and output
position.view(sim=fuzzy_plane_control_sys)
plt.title("Yoke Position (cm)")
angle.view(sim=fuzzy_plane_control_sys)
plt.title("Plane Angle (DEG)")
velocity.view(sim=fuzzy_plane_control_sys)
plt.title("Plane Velocity (km/h)")
plt.show(block=True)