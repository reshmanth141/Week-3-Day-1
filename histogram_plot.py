"""Create a histogram and compare different bin counts."""

import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(42)
data = np.concatenate(
	[
		rng.normal(loc=50, scale=10, size=500),
		rng.normal(loc=75, scale=6, size=300),
	]
)

bin_counts = [8, 20, 40]
fig, axes = plt.subplots(1, len(bin_counts), figsize=(15, 4), sharey=True)

for axis, bins in zip(axes, bin_counts):
	axis.hist(data, bins=bins, color="steelblue", edgecolor="white")
	axis.set_title(f"{bins} bins")
	axis.set_xlabel("Value")
	axis.grid(axis="y", alpha=0.25)

axes[0].set_ylabel("Frequency")
fig.suptitle("Histogram of Sample Numeric Data")
fig.tight_layout()
plt.show()
