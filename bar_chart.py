import matplotlib.pyplot as plt


categories = ["A", "B", "C", "D"]
values = [10, 25, 15, 30]

plt.bar(categories, values, color="steelblue")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart")
plt.tight_layout()
plt.show()