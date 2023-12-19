# Install and load ggplot2 if not already installed
# install.packages("ggplot2")
library(ggplot2)
data <- data.frame(
  x_from = c(0, 0.267668, 0.280006, 0.441577, 0.444207, 0.595301, 0.600797, 0.678262, 0.698191, 0.737838, 0.747383, 0.783663, 0.787369, 0.856423, 0.863302, 0.868581, 0.873742, 0.948518, 0.956921),
  x_to = c(0.267668, 0.280006, 0.441577, 0.444207, 0.595301, 0.600797, 0.678262, 0.698191, 0.737838, 0.747383, 0.783663, 0.787369, 0.856423, 0.863302, 0.868581, 0.873742, 0.948518, 0.956921, 1.000000),
  f_x = c(0, 0.012338, 0, 0.002631, 0, 0.005495, 0, 0.019929, 0, 0.009544, 0, 0.003706, 0, 0.006880, 0, 0.005160, 0, 0.008403, 0)
)

# Set the width and height of the plot image
options(repr.plot.width=16)

# Create a step plot with colors using ggplot2
ggplot(data, aes(x = x_from, y = f_x)) +
  geom_step(direction = "hv", linetype = "solid", color = "blue") +
  labs(x = "time pos (time / total time)", y = "length ratio (length / total time)", title = "When did loadings happen and their length ratios (length / total time)") +
  theme_minimal() +
  theme(aspect.ratio = 2/5) +
  theme(plot.title = element_text(size = 28),
        axis.text = element_text(size = 20),  # Adjusts the size of axis labels
        axis.title = element_text(size = 20)  # Adjusts the size of axis titles)
        ) +
  coord_cartesian(ylim = c(0, 1))

# Save the plot into a png
ggsave("loading_times.png", width = 10, height = 2.5)  # Adjust width and height as needed
