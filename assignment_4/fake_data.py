import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate fake data
data = {
    "rainfall_mm": np.random.normal(loc=50, scale=20, size=100),  # Average rainfall 50mm, standard deviation 20mm
    "rainy_days": np.random.randint(0, 15, size=100),              # Rainy days range from 0 to 15 days
    "mushroom_species": np.random.choice(['Shiitake', 'Oyster', 'Chicken Leg', 'King Oyster'], size=100),  # Randomly choose mushroom species
    "growth_rate_g": np.random.normal(loc=200, scale=50, size=100),  # Average growth rate 200g, standard deviation 50g
    "harvest_time": pd.date_range(start='2023-01-01', periods=100, freq='D')  # Harvest time
}

# Create DataFrame
df_fake = pd.DataFrame(data)

# Save as CSV file
df_fake.to_csv('fake_rain_mushrooms.csv', index=False)