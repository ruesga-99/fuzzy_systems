# Fuzzy Air Conditioning 🌬️
This directory contains a fuzzy expert system which controls the voltage applied to an air conditioning unit taking into consideration the room temperature and relative humidity parameters.

## Fuzzy Sets 
**Input: Room Temperature**

*Universe: [] °C*
- Low: 
- Medium:
- High:

**Input: Relative Humidity**

*Universe: [] %*
- Low: 
- Medium:
- High:

**Output: Applied Voltage**

*Universe: [] V*
- Low: 
- Low_Medium:
- Medium:
- High_Medium:
- High:

## Set of Rules

| Room Temperature | Relative Humidity | Applied Voltage    |
|----------|-------|-------------|
| Low    | Low   |   | 
| Low    | Medium |   | 
| Low     | High |          | 
| Medium      | Low    |  | 
| Medium    | Medium |  | 
| Medium     | High | | 
| High  | Low   | |
| High     | Medium |  |
| High     | High  |  |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ruesga-99/fuzzy_air_conditioning.git
   
2. Install dependencies:
   ```bash
   pip install numpy
   pip install scikit-fuzzy
   pip install matplotlib
