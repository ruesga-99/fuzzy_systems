# Fuzzy Traffic Light 🚦
This directory contains a fuzzy expert system for a smart traffic light controller, which considers factors such as traffic density, time of the day and weather conditions (rain).

## Fuzzy Sets 
**Input: Traffic Density**

*Universe: [0 - 300] vehicles per hour*
- Low: [0, 100]
- Medium: [50, 200]
- High: [150, 300]

**Input: Time of Day**

*Universe: [6:00 - 20:00] hrs*
- Morning: [6:00, 8:00]
- PeakHours: [7:30, 9:00] & [17:00, 19:00]
- ValleyTime: [8:40, 17:15]
- Night: [18:00, 20:00]

**Input: Weather Conditions**

*Universe: [0 - 50] mm/hr*
- Light: [0, 5]
- Moderate: [0, 20]
- Heavy: [10, 50]

**Output: Traffic Light Time**

*Universe: [1 - 60] sec*
- Short: [1, 25]
- Medium: [20, 45]
- Long: [40, 60]

## Set of Rules

| Traffic Density | Time of Day | Weather Conditions | Traffic Light Time |
|----------------|-------------|--------------------|-------------------|
| Low            | Morning     | Light             | Short              |
| Low            | Morning     | Moderate          | Short              |
| Low            | Morning     | Heavy             | Medium             |
| Low            | PeakHour    | Light             | Medium             |
| Low            | PeakHour    | Moderate          | Medium             |
| Low            | PeakHour    | Heavy             | Long               |
| Low            | ValleyTime  | Light             | Short              |
| Low            | ValleyTime  | Moderate          | Short              |
| Low            | ValleyTime  | Heavy             | Medium             |
| Low            | Night       | Light             | Short              |
| Low            | Night       | Moderate          | Short              |
| Low            | Night       | Heavy             | Medium             |
| Medium         | Morning     | Light             | Medium             |
| Medium         | Morning     | Moderate          | Medium             |
| Medium         | Morning     | Heavy             | Long               |
| Medium         | PeakHour    | Light             | Medium             |
| Medium         | PeakHour    | Moderate          | Long               |
| Medium         | PeakHour    | Heavy             | Long               |
| Medium         | ValleyTime  | Light             | Medium             |
| Medium         | ValleyTime  | Moderate          | Medium             |
| Medium         | ValleyTime  | Heavy             | Long               |
| Medium         | Night       | Light             | Medium             |
| Medium         | Night       | Moderate          | Medium             |
| Medium         | Night       | Heavy             | Long               |
| High           | Morning     | Light             | Long               |
| High           | Morning     | Moderate          | Long               |
| High           | Morning     | Heavy             | Long               |
| High           | PeakHour    | Light             | Long               |
| High           | PeakHour    | Moderate          | Long               |
| High           | PeakHour    | Heavy             | Long               |
| High           | ValleyTime  | Light             | Medium             |
| High           | ValleyTime  | Moderate          | Long               |
| High           | ValleyTime  | Heavy             | Long               |
| High           | Night       | Light             | Medium             |
| High           | Night       | Moderate          | Long               |
| High           | Night       | Heavy             | Long               |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ruesga-99/fuzzy_traffic_light.git
   
2. Install dependencies:
   ```bash
   pip install numpy
   pip install scikit-fuzzy
   pip install matplotlib
