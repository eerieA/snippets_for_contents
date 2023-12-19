import matplotlib.pyplot as plt
import numpy as np

# Data
x_from = np.array([0, 0.267668, 0.280006, 0.441577, 0.444207, 0.595301, 0.600797, 0.678262, 0.698191, 0.737838, 0.747383, 0.783663, 0.787369, 0.856423, 0.863302, 0.868581, 0.873742, 0.948518, 0.956921])
x_to = np.array([0.267668, 0.280006, 0.441577, 0.444207, 0.595301, 0.600797, 0.678262, 0.698191, 0.737838, 0.747383, 0.783663, 0.787369, 0.856423, 0.863302, 0.868581, 0.873742, 0.948518, 0.956921, 1.0])
f_x = np.array([0, 0.012338, 0, 0.002631, 0, 0.005495, 0, 0.019929, 0, 0.009544, 0, 0.003706, 0, 0.006880, 0, 0.005160, 0, 0.008403, 0])

# Plot step function with filled areas
plt.figure(figsize=(20, 8)) # Adjust the width and height as needed
plt.fill_between(x_to, 0, f_x, step="pre", alpha=0.1, color='blue')
plt.step(np.concatenate([x_from, x_to[-1:]]), np.concatenate([f_x, [f_x[-1]]]), where='post', linestyle='solid', color='blue', linewidth=3)

# Set labels and title
plt.xlabel('time pos (time / total time)', fontsize=18)
plt.ylabel('length ratio (length / total time)', fontsize=18)
plt.title('When did loadings happen and their length ratios (length / total time)', fontsize=24)

# Set y-axis range
plt.ylim([0, 0.5])

# Increase tick label font size
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

# Set axis and function line thicker
plt.gca().spines['bottom'].set_linewidth(2)
plt.gca().spines['left'].set_linewidth(2)
plt.gca().spines['top'].set_linewidth(2)
plt.gca().spines['right'].set_linewidth(2)

# Show the plot
plt.savefig('time_plot.png')
plt.show()
