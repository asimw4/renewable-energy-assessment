import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
data = pd.read_csv(r"C:\Users\asimw\Downloads\demandfordistributedrenewableenergygenerationinpakistan.csv")

# Clean the dataset
data.dropna(inplace=True)  # Handling missing values

# Use the correct column names from the dataset
data['Total KVA  Connected'] = pd.to_numeric(data['Total KVA  Connected'].replace('-', 0).replace('_', 0), errors='coerce')
data['Maximum Load on Incoming (Amp)'] = pd.to_numeric(data['Maximum Load on Incoming (Amp)'].replace('-', 0).replace('_', 0), errors='coerce')

# Calculate solar and wind potential
data['Solar Potential (MWh)'] = data['Total KVA  Connected'].apply(lambda x: x * 1.5 if pd.notnull(x) else 0)
data['Wind Potential (MWh)'] = data['Maximum Load on Incoming (Amp)'].apply(lambda x: x * 0.75 if pd.notnull(x) else 0)

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

# Check and create a new directory if necessary
new_directory = r"C:\Users\asimw\Documents\EnergyEfficiency"
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

# Save the updated DataFrame to a CSV file in the new directory
save_path = os.path.join(new_directory, 'updated_dataframe_with_potential.csv')
data.to_csv(save_path, index=False)
print(f"CSV file saved to: {save_path}")

