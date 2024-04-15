"""Insectoid graphs. Elias Hedberg 2024."""

import matplotlib.pyplot as plt
import pandas as pd


def load_csv_to_df(file_path):
    df = pd.read_csv(file_path, header=1, skipfooter=1, engine="python")
    df.replace("−", "-", regex=True, inplace=True)
    df.replace(",", ".", regex=True, inplace=True)
    df = df.astype(float)
    print(df.dtypes)

    return df

def plot_x_y(data):
    plt.plot(data["x"], data["y"])
    plt.axis((min(data["x"]) - 1, max(data["x"]) + 1, min(data["y"]) - 1, max(data["y"]) + 1))
    plt.xlabel("Wing movement in x axis")
    plt.ylabel("Wing movement in y axis")
    #plt.axis((0, 6, 0, 20))

    plt.show()

def main():
    data = load_csv_to_df("test_data.csv")
    print(data)
    plot_x_y(data)


if __name__ == "__main__":
    main()
