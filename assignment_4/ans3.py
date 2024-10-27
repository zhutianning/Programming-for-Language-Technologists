import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
df = pd.read_csv('./adjusted_fake_rain_mushrooms_with_high_noise.csv')

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(df['rainfall_mm'], df['growth_rate_g'])

# Calculate the mean of the coefficients
mean_slope = np.mean(slope)
mean_intercept = np.mean(intercept)

# Print the results
print(f'Slope: {slope}')
print(f'Intercept: {intercept}')
print(f'Mean Slope: {mean_slope}')
print(f'Mean Intercept: {mean_intercept}')
print(f'R-squared: {r_value**2}')
print(f'P-value: {p_value}')
print(f'Standard Error: {std_err}')

# Create a scatter plot with the regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='rainfall_mm', y='growth_rate_g', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Linear Regression: Rainfall vs Mushroom Growth Rate')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Mushroom Growth Rate (g)')
plt.grid()
# plt.show()
# save it to png
plt.savefig('adjusted_fake_rain_mushrooms_with_high_noise.png',dpi=400,bbox_inches='tight')
print("png saved as 'adjusted_fake_rain_mushrooms_with_high_noise.png")