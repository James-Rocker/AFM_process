import os
import matplotlib.pyplot as plt

# Plotting configs
plt.figure(1)
plt.figure(2)
plt.figure(3)
plt.figure(4)
a, b, c, d = 0, 0, 0, 0

# folder path
dir_path = "./HepG2/curves"

# list file and directories
files = os.listdir(dir_path)
print(f"files in path are: {files}")

for file in files:
    file_split = file.split("_")
    box = file_split[0][-1:]
    cant = file_split[1][-1:]

    # needs a try/except for index errors
    sequence = file_split[5][:2]

    with open("Processed_retraction_curve/Cantilever size and parameters.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(",")
            if line[0] == box and line[1][0] == cant:
                radius = float(line[2])

    with open("HepG2/curves/" + file) as f:
        lines = f.readlines()
        lines = lines[75:]
        x = []
        y = []
        for line in lines:
            numbers = line.split()
            first_number = float(numbers[0])
            second_number = float(numbers[1])
            x.append(first_number)
            y.append(second_number)

    # Rescale
    for i in range(len(x)):
        x[i] = x[i] * 10**6
        y[i] = y[i] * 10**9

    # Translation
    x_trans = x[0]
    for i in range(len(x)):
        x[i] = x[i] - x_trans

    # Division by sphere size
    for i in range(len(x)):
        x[i] = x[i] / radius

    # Default black colour
    colour = "black"
    if sequence == "1s":
        plt.figure(1)
        a += 1
        d += 1
    elif sequence == "30":
        colour = "blue"
        plt.figure(2)
        b += 1
        d += 1
    elif sequence == "60":
        colour = "red"
        plt.figure(3)
        c += 1
        d += 1
    else:
        print(f"Different time. Actual time was {sequence}")

    # Individual graph data is plotted here
    plt.plot(x, y, linewidth=1, color=colour)

    # For the total graph
    plt.figure(4)
    plt.plot(x, y, linewidth=1, color=colour)

# metadata for plotting
plot_key_list = [
    {1: {"group": "1s", "count": a}},
    {2: {"group": "30s", "count": b}},
    {3: {"group": "60s", "count": c}},
    {4: {"group": "1s, 30s, 60s", "count": d}},
]

for meta_data in plot_key_list:
    for key, value in meta_data.items():
        plt.figure(key)
        plt.title(f"{value['group']} ({value['count']} plots)", fontsize=14)
        plt.xlabel("Height (um)", fontsize=14)
        plt.ylabel("Force per Radius (nN)", fontsize=14)
        plt.ylim([-6, 2])
        if value["group"] is "1s, 30s, 60s":
            plt.savefig(f"output/total_output")
        else:
            plt.savefig(f"output/{value['group']}_output")
