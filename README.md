# Fuzzy Logic Systems
This repository contains different fuzzy expert systems applicable to IoT devices.
Each model considers factors differnet real-life continuous factors.

## Theory Behind Fuzzy Logic

Fuzzy logic is a branch of mathematics and artificial intelligence that models uncertainty and imprecision in data. It is a powerful tool for representing and manipulating ambiguous concepts, making it ideal for systems requiring nuanced decision-making.

At its core, fuzzy logic relies on the concept of fuzzy sets, where elements have gradual membership functions. This allows an element to belong to multiple sets simultaneously, unlike classical binary logic that imposes strict boundaries. This flexibility makes fuzzy logic suitable for handling uncertainty in complex systems.

Fuzzy logic employs various operators and rules to manipulate fuzzy sets effectively. Common operators include conjunction, disjunction, and negation. Logical rules such as *modus ponens* and *modus tollens* further enhance the system’s ability to model complex behaviors.

### Classic Logic vs Fuzzy Logic

| Feature     | Classic Logic         | Fuzzy Logic              |
|-------------|-----------------------|--------------------------|
| Membership  | Binary (0 or 1)       | Gradual (0 to 1)         |
| Precision   | Strict and exact      | Flexible and approximate |
| Application | Well-defined problems | Real-world uncertainty   |   

### Mamdani Algorithm

The Mamdani algorithm is one of the most widely used fuzzy inference methods. It provides a framework for decision-making by applying fuzzy logic rules to input data and generating outputs that reflect real-world scenarios. This algorrithm includes the following steps:
1. Define input and output linguistic variables, including their numeric ranges and their membership functions (MF).
2. Define a set of rules that represents the control strategy for the system.
3. *Fuzzify* the input values, in this step each input value will be assigned to its category according to the defined membership functions and set of rules.
4. Analyze the inference to determine the strength of the activated rules.
5. *De-fuzzify* the output values using a center of gravity centroid and determine the action to be executed.

### Membership Functions

Membership functions define how each input maps to a degree of membership within a fuzzy set. Common types include:
- Triangular
  - Lambda Function
- Trapezoidal
  - Gamma Function
  - L-Function
- Gaussian
- Sigmoid

### Real Life Applications
Fuzzy systems are useful whenever a process has a high complexity and no precise mathematical models are availiable, thus
fuzzy systems are powerful tools in different indusrty-environments and IoT systems such as:
- Temperature control systems.
- Light control systems.
- Fuel efficiency systems.
- Robotic control applications.
- Autonomous driving.
- Writing systems.

## List of Implemented Models
**Basic Models**
<dl>
  <dd> &nbsp&nbsp ✅ Fuzzy Traffic Light </dd>
  <dd> &nbsp&nbsp ✅ Fuzzy Plane Controller </dd>
  <dd> &nbsp&nbsp ✅ Fuzzy Air Conditioning </dd>
  <dd> &nbsp&nbsp 📆 Smart Illumination System </dd>
  <dd> &nbsp&nbsp 💡 Inverted Pendulum </dd>
</dl>

> [!IMPORTANT]
> **Advanced Fuzzy Systems: Adaptive Neuro-Fuzzy Inference System (ANFIS)**
> 
> For more sophisticated applications, this repository links to a dedicated implementation of ANFIS (Adaptive Neuro-Fuzzy Inference System), a hybrid model that combines fuzzy logic with neural networks. ANFIS enhances traditional fuzzy systems by:
> - *Learning capability*: Automatically optimizes fuzzy rules and membership functions through training data.
> - *Adaptation*: Dynamically adjusts to changing environments, making it ideal for IoT systems with real-time data streams.
> - *Precision*: Balances interpretability (fuzzy logic) with predictive accuracy (neural networks).
> 
> Explore the [ANFIS](https://github.com/ruesga-99/anfis) repository here to see how machine learning and fuzzy logic synergize in complex decision-making scenarios. Contributions and feedback are welcome!

## Emoji Key
✅ (Completed): This emoji is used to mark tasks that have been finished and require no further work.

📆 (Planned): This emoji is used for tasks that are planned for the future, indicating they are on the work calendar. The corresponding file does not exist within the repository.

🚧 (Under Construction): This emoji indicates tasks that have been implemented but still need further improvements or adjustments. There is already a corresponding file within the repository but hasn't been fully developed.

💡 (Planning Ongoing): This emoji is used for sections that haven't been completely defined on their components. 

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ruesga-99/fuzzy_traffic_light.git
   ```
   
2. Install dependencies:
   ```bash
   pip install numpy
   pip install scikit-fuzzy
   pip install matplotlib
   ```
> [!NOTE]
> [Scikit-Fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy) depends on:
>  - Matplotlib >= 3.1
>  - NumPy >= 1.6
>  - SciPy >= 0.9
>  - NetworkX >= 1.9

## Contributions

Feel free to contribute to this repository adding your own models or upgrading the existing ones!

To contribute a solution:

1. Clone the repository.
2. Create a new subdirectory for your model if necessary.
3. Develop your model in the corresponding directory.
4. Update the model's README.md file with a brief description.
5. Submit a pull request for review.
