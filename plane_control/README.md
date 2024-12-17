# Fuzzy Plane Control ✈️
This directory contains a fuzzy expert system which controls the yoke's position of a plane according to the current velocity and 
flight path angle.

## Fuzzy Sets 
**Input: Velocity**

*Universe: [0 - 1000] km/h*
- Low: [0, 450, 500]
- OK: [450, 550, 700]
- High: [550, 850, 1000]

**Input: Angle**

*Universe: [-10 - 10] DEG*
- Down: [-10, -5, 0]
- Level: [-5, 0, 5]
- Up: [0, 5, 10]

**Output: Traffic Light Time**

*Universe: [0 - 10] cm*
- Low: [0, 4]
- Low_Medium: [2, 4, 6]
- Medium: [4, 6, 8]
- High_Medium: [6, 8, 10]
- High: [8, 10]

## Set of Rules

| Velocity | Angle | Position    |
|----------|-------|-------------|
| High     | Up    | Low_Medium  | 
| High     | Level | Low_Medium  | 
| High     | Down  | Low         | 
| OK       | Up    | High_Medium | 
| OK       | Level | Medium      | 
| OK       | Down  | Low_Medium  | 
| Low      | Up    | Low_Medium  |
| Low      | Level | Low_Medium  |
| Low      | Down  | Low         |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ruesga-99/fuzzy_plane_control.git
   
2. Install dependencies:
   ```bash
   pip install numpy
   pip install scikit-fuzzy
   pip install matplotlib
