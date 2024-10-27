"""
Rain (X) and mushrooms (Y) as examples to illustrate different scenarios of correlation and causation:

1. X -> Y
   Rain (X) directly causes mushroom growth (Y).
   Rain provides the necessary moisture for mushrooms, promoting their growth.

2. X -> Z -> Y
   Rain (X) increases soil moisture (Z), and soil moisture (Z) promotes mushroom growth (Y).
   Here, soil moisture is an intermediate variable.

3. X <- Y
   This scenario is unlikely in the relationship between rain and mushrooms, as mushrooms don't cause rainfall.

4. X <- Z -> Y
   Temperature changes (Z) might simultaneously affect rainfall (X) and mushroom growth (Y).
   For example, warm and humid weather might both increase rainfall and create favorable conditions for mushroom growth.

5. X <-> Y
   In this case, there might be a complex ecological relationship between rain and mushrooms.
   For instance, rain promotes mushroom growth, while mushrooms improve soil structure through decomposition of organic matter, thereby influencing local water cycles.

6. X and Y have no causal relationship, merely a coincidence
   In a particular area, people might observe a correlation between increased rainfall and increased mushroom numbers, but this could be just a coincidence.
   In reality, the increase in mushrooms might be due to other factors such as temperature, humidity, or human cultivation.

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# read csv file
df = pd.read_csv('howell1.csv')

# set style
sns.set_style("whitegrid")
# create a scatter plot and add a line
sns.regplot(data=df, x='height', y='weight', scatter=True, ci=None)
plt.title('height and weight relationship')
plt.xlabel('height (cm)')
plt.ylabel('weight (kg)')

# save it to png
plt.savefig('height_weight_relationship.png',dpi=400,bbox_inches='tight')
print("png saved as 'height_weight_scatter.png'")

def linear_regression(df, x_par, y_par):
    slope, intercept, r_value, p_value, std_err = stats.linregress(df[x_par], df[y_par])

    return {
        'Coefficient': slope,
        'Intercept': intercept,
        'R-squared': r_value**2,
        'P-value': p_value
    }

print(linear_regression(df,'height','weight'))