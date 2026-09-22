import matplotlib.pyplot as plt


days = [1, 2, 3, 4, 5, 6, 7]
temperatures = [22, 24, 23, 26, 27, 25, 28]

plt.figure(figsize=(8, 5))
plt.plot(days, temperatures, marker="o", linewidth=2, color="steelblue")
plt.title("Daily Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.xticks(days)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
