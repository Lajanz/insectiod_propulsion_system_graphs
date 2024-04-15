import matplotlib.pyplot as plt
import numpy as np


def gen_categories(wings, springs):
    # Categories

    x = []
    #x = list(range((len(wings)))) * len(springs)
    for i in range(len(wings)):
        x.extend([i] * len(springs))

    y =[]
    for i in range(len(wings)):
        y.extend([i] * len(springs))

    y = list(range((len(springs)))) * len(wings)
    return x, y


def gen_plot(wings, springs, x, y, lift):
    # Create plot
    plt.figure(figsize=(8, 6))
    sc = plt.scatter(x, y, s=lift, c=lift, cmap="viridis", alpha=1)  # Use values for color and size

    # Add color bar
    plt.colorbar(sc, label="Lift (g)")

    # Customize the plot
    plt.xticks(ticks=np.arange(len(wings)), labels=wings)
    plt.yticks(ticks=np.arange(len(springs)), labels=springs)
    plt.xlabel("Wing type")
    plt.ylabel("Spring")
    plt.title("Scatter plot of maxiumum lift (g)")

    plt.grid(True)
    plt.show()

def main():
    wings = ["50%", "80%", "100%", "Wide", "Long"]
    springs = ["No spring", "Soft", "Medium", "Hard"]
    # pattern is [50% no spring, 50% soft, 50% medium, 50% hard, 80% no spring, ... , 100% hard]
    lift = (np.arange(len(springs) * len(wings)) * 1000).reshape(len(springs),len(wings))

    x, y = gen_categories(wings, springs)
    gen_plot(wings, springs, x, y, lift)

if __name__ == "__main__":
    main()
