import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


# File path for the TensorBoard logs
log_file = '/home/ye/rl_rvo_nav/rl_rvo_nav/policy_train/runs/experiment_r10_18/events.out.tfevents.1701619123.Ye-PC.154015.0'

def read_tensorboard_data(log_file):
    data = []
    for e in tf.compat.v1.train.summary_iterator(log_file):
        for v in e.summary.value:
            data.append({
                "Time": e.wall_time,
                "Step": e.step,
                "Metric": v.tag,
                "Value": v.simple_value
            })
    return pd.DataFrame(data)

tb_data = read_tensorboard_data(log_file)

csv_file = 'tensorboard_data.csv'
tb_data.to_csv(csv_file, index=False)

print(f"Data saved to {csv_file}")

# # Determine the layout of subplots
# num_metrics = len(tb_data)
# cols = 2
# rows = math.ceil(num_metrics / cols)

# # Plotting each metric
# plt.figure(figsize=(15, 5 * rows))

# for i, (metric, values) in enumerate(tb_data.items(), 1):
#     steps, vals = zip(*values)
#     plt.subplot(rows, cols, i)
#     plt.plot(steps, vals, label=metric)
#     plt.title(metric)
#     plt.xlabel('Steps')
#     plt.ylabel('Value')
#     plt.legend()
#     plt.grid(True)

# plt.tight_layout()
# plt.show()
