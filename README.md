# Renewable Energy Assessment

## Overview
This project involves the analysis and visualization of solar and wind energy potential across various grid stations in Pakistan. The goal is to identify key areas for deploying renewable energy solutions and contribute to the ongoing efforts to mitigate Pakistan's energy crisis by reducing reliance on fossil fuels.

## Project Goals
- Assess the solar and wind energy potential of various grid stations in Pakistan.
- Visualize the distribution of solar and wind energy potential.
- Provide insights to support policy-making and investment decisions aimed at promoting renewable energy.

## Project Steps

### Step 1: Load the Dataset
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
data = pd.read_csv(r"C:\Users\asimw\Downloads\demandfordistributedrenewableenergygenerationinpakistan.csv")
```
We start by loading the dataset containing information on grid stations and their energy consumption.

### Step 2: Clean the Dataset
```python
# Clean the dataset
data.dropna(inplace=True)  # Handling missing values

# Use the correct column names from the dataset
data['Total KVA  Connected'] = pd.to_numeric(data['Total KVA  Connected'].replace('-', 0).replace('_', 0), errors='coerce')
data['Maximum Load on Incoming (Amp)'] = pd.to_numeric(data['Maximum Load on Incoming (Amp)'].replace('-', 0).replace('_', 0), errors='coerce')
```
We clean the dataset by handling missing values and converting relevant columns to numeric types for analysis.

### Step 3: Calculate Solar and Wind Potential
```python
# Calculate solar and wind potential
data['Solar Potential (MWh)'] = data['Total KVA  Connected'].apply(lambda x: x * 1.5 if pd.notnull(x) else 0)
data['Wind Potential (MWh)'] = data['Maximum Load on Incoming (Amp)'].apply(lambda x: x * 0.75 if pd.notnull(x) else 0)
```
We calculate the potential for solar and wind energy based on the connected KVA and maximum incoming load respectively.

### Step 4: Visualize the Results
```python
# Visualize the results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(data['Solar Potential (MWh)'], bins=30, kde=True)
plt.title('Distribution of Solar Potential (MWh)')
plt.xlabel('Solar Potential (MWh)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
sns.histplot(data['Wind Potential (MWh)'], bins=30, kde=True)
plt.title('Distribution of Wind Potential (MWh)')
plt.xlabel('Wind Potential (MWh)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
```
We create histograms to visualize the distribution of solar and wind energy potential.

### Step 5: Save the Updated DataFrame
```python
# Check and create a new directory if necessary
new_directory = r"C:\Users\asimw\Documents\EnergyEfficiency"
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

# Save the updated DataFrame to a CSV file in the new directory
save_path = os.path.join(new_directory, 'updated_dataframe_with_potential.csv')
data.to_csv(save_path, index=False)
print(f"CSV file saved to: {save_path}")
```
We save the updated dataset, including the calculated potentials, to a new CSV file.

## Insights and Conclusions
The results of this project provide a clear visualization of the potential for solar and wind energy across various grid stations in Pakistan. Key insights include:
- **Solar Potential:** High potential in grid stations such as Nur Pur Sethi and Talagang, indicating significant opportunities for solar energy deployment.
- **Wind Potential:** Grid stations like Talagang and Murree show high potential for wind energy, suggesting ideal locations for wind energy projects.

These insights can support policy-makers and investors in making informed decisions to promote renewable energy projects, ultimately contributing to the mitigation of Pakistan's energy crisis.

## Files Included
- **EnergyEfficiency.py:** The Python script containing the full code for the project.
- **Project Visualizations.png:** A visualization of the solar and wind energy potential distributions.
- **demandfordistributedrenewableenergygenerationinpakistan.csv:** The original dataset used for the analysis.
- **updated_dataframe_with_potential.csv:** The updated dataset including the calculated solar and wind energy potentials.

## How to Run the Project
1. Clone the repository to your local machine.
2. Ensure you have the required libraries installed (`pandas`, `matplotlib`, `seaborn`).
3. Run the `EnergyEfficiency.py` script to perform the analysis and generate visualizations.
4. Check the `updated_dataframe_with_potential.csv` file in the specified directory for the updated dataset.
