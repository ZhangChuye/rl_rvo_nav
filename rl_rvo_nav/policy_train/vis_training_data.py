import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/ye/rl_rvo_nav/rl_rvo_nav/policy_train/tensorboard_data.csv")

# Separating the data based on different metrics for analysis
metrics = df['Metric'].unique()

# Plotting and saving each metric in a separate file
for metric in metrics:
    # Filter data for the current metric
    metric_data = df[df['Metric'] == metric]

    # Create a new figure for each metric
    plt.figure(figsize=(10, 5))
    
    # Plotting
    plt.plot(metric_data['Step'], metric_data['Value'])
    plt.title(metric)
    plt.xlabel('Training Steps')
    plt.ylabel('Value')
    plt.grid(True)

    # Save the figure with a filename based on the metric
    filename = f"/home/ye/rl_rvo_nav/rl_rvo_nav/policy_train/plots/{metric.replace('/', '_')}.png"
    plt.savefig(filename)

    # Close the plot to free up memory
    plt.close()
