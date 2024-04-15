import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd


def load_data(path_to_csv):
    df = pd.read_csv(path_to_csv, header=1, skipfooter=11, engine="python")
    df.replace("--", np.NaN, regex=True, inplace=True)
    df.replace("No peak", np.NaN, regex=True, inplace=True)
    df.replace("−", "-", regex=True, inplace=True)
    df.replace(",", ".", regex=True, inplace=True)
    df.replace("0.1 - 0.3", "0.2", regex=True, inplace=True)
    df.replace("0.2 - 0.4", "0.3", regex=True, inplace=True)

    #df = df.astype(float)
    df = df.drop(df.columns[[0, 1, 2, 3]], axis=1)
    #df = df.to_numpy()
    print(df)


def gen_categories(wings, springs):
    # Categories

    x = []
    # x = list(range((len(wings)))) * len(springs)
    for i in range(len(wings)):
        x.extend([i] * len(springs))

    y = []
    for i in range(len(wings)):
        y.extend([i] * len(springs))

    y = list(range((len(springs)))) * len(wings)
    return x, y


def gen_plot(wings, springs, x, y, lift):
    # Create plot
    plt.figure(figsize=(8, 6))
    plt.grid(True, zorder=-1.0)
    sc = plt.scatter(x, y, s=lift, c=lift, cmap="YlOrRd", alpha=1)  # Use values for color and size

    # Add color bar
    plt.colorbar(sc, label="Lift (g)", format=mticker.FixedFormatter([1.5 * i/6 for i in range(6)]))
    # Customize the plot
    plt.xticks(ticks=np.arange(len(wings)), labels=wings)
    plt.yticks(ticks=np.arange(len(springs)), labels=springs)
    plt.xlabel("Wing type")
    plt.ylabel("Spring")
    plt.title("Scatter plot of maxiumum lift (g)")
    
    plt.margins(0.2)


    plt.show()

def main():
    load_data("liftdata.csv")
    wings = ["50%", "80%", "100%", "Wide", "Long"]
    springs = ["No spring", "Soft", "Medium", "Hard"]
    # pattern is [50% no spring, 50% soft, 50% medium, 50% hard, 80% no spring, ... , 100% hard]
    # lift = (np.arange(len(springs) * len(wings)) * 1000).reshape(len(springs),len(wings))
    lift = [0.72, 0.60, 0.85, 0.52,
            0.70, 1.39, 0.93, 0.40,
            0.50, 1.30, 0.39, 0,
            0.90, 0.80, 0.50, 0,
            0, 0, 0, 0]
    lift = [i * 2000 for i in lift]


    x, y = gen_categories(wings, springs)
    gen_plot(wings, springs, x, y, lift)

if __name__ == "__main__":
    main()
