# Fitness Member Analysis System

## Overview
The **Fitness Member Analysis System** is a Python-based program designed to analyze and track gym members' fitness details. The system calculates Body Mass Index (BMI), evaluates fitness levels based on resting heart rates, and provides personalized workout recommendations.

## Features
- Collects data for multiple gym members.
- Validates user input to ensure accurate data entry.
- Calculates BMI and categorizes members into different BMI groups.
- Assesses fitness levels based on resting heart rates.
- Generates personalized workout recommendations.
- Allows trainers to:
  - View a summary of all members' fitness details.
  - Identify members who require physician approval before training.
  - Retrieve specific member details.
  - Exit the program.

## Installation & Usage
1. Ensure you have Python installed (version 3.6 or later recommended).
2. Run the script in a Python environment or terminal:
   ```bash
   python fitness_analysis.py
   ```
3. Follow the on-screen prompts to input member details and analyze fitness levels.

## Input Data
For each member, the system requires:
- **Name**
- **Weight (kg)** (Valid range: 20 - 200 kg)
- **Height (cm)** (Valid range: 50 - 250 cm)
- **Resting Heart Rate (bpm)** (Valid range: 30 - 200 bpm)

## BMI Categories
- **Underweight**: BMI < 18.5
- **Healthy**: 18.5 ≤ BMI < 24.9
- **Overweight**: 24.9 ≤ BMI < 29.9
- **Obese**: BMI ≥ 29.9

## Fitness Levels (Based on Resting Heart Rate)
- **Athlete**: < 60 bpm
- **Good**: 60 - 72 bpm
- **Acceptable**: 73 - 83 bpm
- **Needs Improvement**: ≥ 84 bpm

## Workout Recommendations
- **Underweight/Obese & Needs Improvement**: Mixed workout with cardio emphasis.
- **Athlete & Healthy BMI**: Strength training emphasis.
- **Acceptable Fitness Level**: Balanced workouts.

## Future Enhancements
- Implement a database for storing member data.
- Develop a GUI for a better user experience.
- Add real-time heart rate monitoring integration.

## License
This project is open-source and available for modification and distribution.
