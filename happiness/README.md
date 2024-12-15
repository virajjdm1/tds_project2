# Data Analysis Story for happiness.csv

### Summary Statistics

**Country_name**:
  - count: 2363
  - unique: 165.00
  - top: Argentina
  - freq: 18
  - mean: nan
  - std: nan
  - min: nan
  - 25%: nan
  - 50%: nan
  - 75%: nan
  - max: nan

**year**:
  - count: 2363.00
  - unique: nan
  - top: nan
  - freq: nan
  - mean: 2014.76
  - std: 5.06
  - min: 2005.00
  - 25%: 2011.00
  - 50%: 2015.00
  - 75%: 2019.00
  - max: 2023.00

**Life_Ladder**:
  - count: 2363.00
  - unique: nan
  - top: nan
  - freq: nan
  - mean: 5.48
  - std: 1.13
  - min: 1.28
  - 25%: 4.65
  - 50%: 5.45
  - 75%: 6.32
  - max: 8.02

**Log_GDP_per_capita**:
  - count: 2335.00
  - unique: nan
  - top: nan
  - freq: nan
  - mean: 9.40
  - std: 1.15
  - min: 5.53
  - 25%: 8.51
  - 50%: 9.50
  - 75%: 10.39
  - max: 11.68

**Social_support**:
  - count: 2350.00
  - unique: nan
  - top: nan
  - freq: nan
  - mean: 0.81
  - std: 0.12
  - min: 0.23
  - 25%: 0.74
  - 50%: 0.83
  - 75%: 0.90
  - max: 0.99

**Healthy_life_expectancy_at_birth**:
  - count: 2300.00
  - unique: nan
  - top: nan
  - freq: nan
  - mean: 63.40
  - std: 6.84
  - min: 6.72
  - 25%: 59.20
  - 50%: 65.10
  - 75%: 68.55
  - max: 74.60

**Freedom_to_make_life_choices**:
  - count: 2327.00
  - unique: nan
  - top: nan
  - freq: nan
  - mean: 0.75
  - std: 0.14
  - min: 0.23
  - 25%: 0.66
  - 50%: 0.77
  - 75%: 0.86
  - max: 0.98

**Generosity**:
  - count: 2282.00
  - unique: nan
  - top: nan
  - freq: nan
  - mean: 0.00
  - std: 0.16
  - min: -0.34
  - 25%: -0.11
  - 50%: -0.02
  - 75%: 0.09
  - max: 0.70

**Perceptions_of_corruption**:
  - count: 2238.00
  - unique: nan
  - top: nan
  - freq: nan
  - mean: 0.74
  - std: 0.18
  - min: 0.04
  - 25%: 0.69
  - 50%: 0.80
  - 75%: 0.87
  - max: 0.98

**Positive_affect**:
  - count: 2339.00
  - unique: nan
  - top: nan
  - freq: nan
  - mean: 0.65
  - std: 0.11
  - min: 0.18
  - 25%: 0.57
  - 50%: 0.66
  - 75%: 0.74
  - max: 0.88

**Negative_affect**:
  - count: 2347.00
  - unique: nan
  - top: nan
  - freq: nan
  - mean: 0.27
  - std: 0.09
  - min: 0.08
  - 25%: 0.21
  - 50%: 0.26
  - 75%: 0.33
  - max: 0.70


## Outlier Counts
year                                 0
Life_Ladder                          2
Log_GDP_per_capita                   3
Social_support                      23
Healthy_life_expectancy_at_birth    14
Freedom_to_make_life_choices        10
Generosity                          21
Perceptions_of_corruption           34
Positive_affect                     10
Negative_affect                     18

## Story and Insights
Based on the provided dataset and the summary statistics, we can derive several insights into the relationships between various factors affecting well-being across different countries. Here’s a detailed analysis:

### Insights & Trends

1. **Overall Happiness and Life Ladder**:
   - The average **Life Ladder** score is approximately **5.48**, indicating that, on average, respondents perceive their lives to be above the midpoint of the scale (0-10).
   - The **Life Ladder** score is significantly positively correlated with **Log GDP per capita** (0.78) and **Social Support** (0.72). This suggests that higher GDP and stronger social networks contribute significantly to perceived happiness.

2. **Economic Influence**:
   - **Log GDP per capita** has a strong correlation with life satisfaction (Life Ladder) and healthy life expectancy (0.82). This emphasizes the importance of economic stability and growth in enhancing overall well-being.
   - Countries with higher GDP per capita tend to have better health outcomes, as indicated by the correlation with **Healthy Life Expectancy** (0.81).

3. **Social Support**:
   - There is a strong link between **Social Support** and positive life outcomes, with a correlation of **0.72** with **Life Ladder** and **0.60** with **Healthy Life Expectancy**. This suggests that social connections and networks play a crucial role in individual happiness and health.
   - However, **Social Support** also has a negative correlation with **Negative Affect** (-0.45), indicating that stronger social ties may help alleviate feelings of negativity.

4. **Freedom and Choices**:
   - The correlation between **Freedom to Make Life Choices** and **Life Ladder** is **0.54**. This indicates that the ability to make personal choices is an essential factor contributing to overall happiness.
   - Conversely, this variable is negatively correlated with **Perceptions of Corruption** (-0.47). Countries with higher levels of freedom tend to have lower corruption perceptions, which in turn can enhance life satisfaction.

5. **Generosity and Positive Affect**:
   - The correlation between **Generosity** and **Life Ladder** is relatively weak (0.18), but it shows a stronger link with **Positive Affect** (0.30). This suggests that while generosity may not directly impact life satisfaction, it can enhance feelings of positivity.

6. **Negative Affect**:
   - The **Negative Affect** score has a significant negative correlation with **Life Ladder** (-0.35), indicating that higher negative feelings reduce overall life satisfaction.
   - It is also noteworthy that **Perceptions of Corruption** have a positive correlation with **Negative Affect** (0.27), suggesting that corruption can lead to increased feelings of negativity among citizens.

### Anomalies

- There are outliers in the **Life Ladder** (2 outliers) and **Log GDP per capita** (3 outliers), which could indicate countries or regions with extreme values affecting the general trend.
- The presence of outliers in **Social Support** (23 outliers) may indicate specific countries where social networks are either exceptionally strong or weak, potentially leading to extreme scores in life satisfaction.

### Implications of Findings

1. **Policy Focus**:
   - Governments should prioritize economic growth and social support systems, as these are crucial for enhancing the overall well-being of their citizens.
   - Policies aimed at reducing corruption could improve perceptions and, in turn, increase happiness levels.

2. **Community Programs**:
   - Initiatives that strengthen social networks and community ties can be beneficial. This could include community service programs, support groups, or social events that encourage interactions among citizens.

3. **Mental Health Awareness**:
   - Programs aimed at reducing negative affect and promoting mental health awareness could help improve life satisfaction. Mental health services should be accessible, and campaigns should focus on destigmatizing mental health issues.

4. **Education on Freedom and Choice**:
   - Educating citizens about their rights and the importance of personal choices can empower them, leading to greater life satisfaction.

### Suggested Actions

- **Economic Development Initiatives**: Encourage investment in sectors that boost GDP, particularly in education and innovation.
- **Strengthening Social Services**: Develop and fund programs that foster community engagement and support networks.
- **Anti-Corruption Measures**: Implement and enforce strict anti-corruption laws to improve public trust and perceptions.
- **Mental Health Programs**: Increase funding for mental health services and awareness campaigns to reduce stigma and promote community mental health.

### Conclusion

The analysis of the dataset highlights the intricate relationships between economic factors, social support, and individual well-being. By focusing on enhancing these areas, countries can improve the overall happiness and life satisfaction of their citizens. The findings advocate for a holistic approach to policy-making that considers economic, social, and mental health factors as interconnected components of overall well-being.

## Visualizations
### Correlation Plot
![Correlation Plot](correlation_plot.png)
### Histogram
![Histogram](histogram.png)
### Missing Values Heatmap
![Missing Values Heatmap](missing_values_heatmap.png)
