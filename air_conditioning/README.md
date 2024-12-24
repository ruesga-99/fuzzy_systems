# Fuzzy Air Conditioning 🌬️
This directory contains a fuzzy expert system which controls the voltage applied to an air conditioning unit taking into consideration the room temperature and relative humidity parameters.

## Fuzzy Sets 
**Input: Room Temperature**

*Universe: [20-40] °C*
- Low: [20, 30]
- Medium: [20, 30, 40]
- High: [30, 40]

**Input: Relative Humidity**

*Universe: [70-90] %*
- Low: [70, 80]
- Medium: [70, 80, 90]
- High: [80, 90]

**Output: Applied Voltage**

*Universe: [0-12] V*
- Low: [0, 3]
- Low_Medium: [0, 3, 6]
- Medium: [3, 6, 9]
- High_Medium: [6, 9, 12]
- High: [9, 12]

## Set of Rules

| Room Temperature | Relative Humidity | Applied Voltage |
|------------------|-------------------|-----------------|
| Low              | Low               | Low             | 
| Low              | Medium            | Mid-Low         | 
| Low              | High              | Mid-High        | 
| Medium           | Low               | Low             |  
| Medium           | Medium            | Medium          | 
| Medium           | High              | High            | 
| High             | Low               | Mid-Low         |
| High             | Medium            | Mid-High        |
| High             | High              | High            |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ruesga-99/fuzzy_air_conditioning.git
   
2. Install dependencies:
   ```bash
   pip install numpy
   pip install scikit-fuzzy
   pip install matplotlib
