'''
To adjust the dataset so that rainfall_mm and growth_rate_g have a strong linear regression relationship, we can create a new growth_rate_g based on a linear function of rainfall_mm. This means we will define a linear equation, such as:

{ growth_rate_g = m × rainfall_mm + b + noise }

Explanation:
1. Parameters: We define a slope (m) and an intercept (b) for the linear relationship.
2. Noise: We add some random noise to the growth rate to simulate real-world variability.
Adjusting Growth Rate: The growth_rate_g is recalculated based on the linear equation.
4. Saving the Adjusted Dataset: The adjusted dataset is saved to a new CSV file named adjusted_fake_rain_mushrooms.csv.
'''

import pandas as pd
import numpy as np

# Load the original dataset
df = pd.read_csv('fake_rain_mushrooms.csv')

# Define parameters for the linear relationship
m = 1.5  # slope
b = 10  # intercept

# Create a strong linear relationship with some noise
np.random.seed(42)  # For reproducibility
# noise = np.random.normal(0, 10, size=len(df))  # Small noise
noise = np.random.normal(0, 100, size=len(df))  # Increased noise

# Adjust growth_rate_g based on rainfall_mm
df['growth_rate_g'] = m * df['rainfall_mm'] + b + noise

# Save the adjusted dataset to a new CSV file
# df.to_csv('adjusted_fake_rain_mushrooms.csv', index=False)
# Save the adjusted dataset to a new CSV file
df.to_csv('adjusted_fake_rain_mushrooms_with_high_noise.csv', index=False)

# Display the first few rows of the adjusted dataset
print(df.head())