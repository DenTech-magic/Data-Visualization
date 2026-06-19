import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# PART 1: LOAD DATA AND SET STYLE

# Load the cleaned file and use the first column as row labels
df = pd.read_csv('/home/astrotuk/D/data_02/cleaned_time_series_data.csv', index_col=0)

# Change the text dates into true date objects so they plot in order
df['date'] = pd.to_datetime(df['date'])

# Use a clean grid background style for the plots
sns.set_theme(style="whitegrid")


# PART 2: SET UP THE PLOT WINDOW


# Make a window that holds two plots stacked on top of each other
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))


# CHART 1: TEMPERATURE LINE GRAPH


# Plot a line graph showing temperature changes over time
sns.lineplot(
    data=df, 
    x='date', 
    y='temp_celsius', 
    ax=ax1, 
    color='royalblue', 
    linewidth=1.5
)

# Add titles and labels to the line graph
ax1.set_title('Daily Temperature Trends Across the Year', fontsize=14, fontweight='bold', pad=10)
ax1.set_xlabel('Timeline (Months)', fontsize=12)
ax1.set_ylabel('Temperature (°C)', fontsize=12)



# CHART 2: TEMPERATURE HISTOGRAM

# Plot a bar chart showing how often different temperatures occur
sns.histplot(
    data=df, 
    x='temp_celsius', 
    ax=ax2, 
    color='coral', 
    kde=True, 
    bins=30
)

# Add titles and labels to the histogram chart
ax2.set_title('Frequency Distribution of Temperature Readings', fontsize=14, fontweight='bold', pad=10)
ax2.set_xlabel('Temperature (°C)', fontsize=12)
ax2.set_ylabel('Number of Days (Count)', fontsize=12)

# PART 3: ADJUST AND SAVE


# Fix spacing so labels and titles do not overlap each other
plt.tight_layout()

# Save the final dual chart as a picture file
plt.savefig('temperature_visualization_dashboard.png', dpi=300)

# Show the charts on the screen
plt.show()
