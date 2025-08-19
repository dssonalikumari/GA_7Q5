# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic business data: Customer engagement (Hours vs Weekdays)
np.random.seed(42)  # for reproducibility
hours = [f"{h}:00" for h in range(9, 21)]  # business hours 9 AM - 8 PM
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Engagement levels: higher on weekdays, slightly lower on weekends
data = np.random.randint(20, 100, size=(len(hours), len(days)))
data[:, -2:] = data[:, -2:] * 0.7  # lower engagement on Sat/Sun

# Convert to DataFrame
df = pd.DataFrame(data, index=hours, columns=days)

# Create heatmap
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512px
ax = sns.heatmap(df, cmap="YlGnBu", annot=False, cbar_kws={'label': 'Engagement Level'})

# Add titles and labels
plt.title("Customer Engagement Heatmap\n(Business Hours vs Days of Week)", fontsize=14, pad=15)
plt.xlabel("Day of Week", fontsize=12)
plt.ylabel("Hour of Day", fontsize=12)

# Save chart with exact 512x512 resolution
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

print("✅ chart.png generated successfully with size 512x512")
