import os
import matplotlib.pyplot as plt


def plot_graph(group, file_name, colour, x_vals, y_vals):
    plt.figure()
    plt.title("%s %s plots" % (group, file_name), fontsize=14)
    plt.xlabel("Height (um)", fontsize=14)
    plt.ylabel("Force per Radius (nN)", fontsize=14)
    plt.ylim([-6, 2])
    plt.plot(x_vals, y_vals, linewidth=1, color=colour)
    plt.savefig("output/%s" % file_name)


# folder path
dir_path = "./HepG2/curves"

# list file and directories
files = os.listdir(dir_path)
print(f"files in path are: {files}")

for file in files:
    if file == '.gitignore':
        continue
        
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
        x[i] = x[i] * 10 ** 6
        y[i] = y[i] * 10 ** 9

    # Translation
    x_trans = x[0]
    for i in range(len(x)):
        x[i] = x[i] - x_trans

    # Division by sphere size
    for i in range(len(x)):
        x[i] = x[i] / radius

    if sequence == "1s":
        plot_graph(group=sequence, file_name=file[:-4], colour='black', x_vals=x, y_vals=y)
    elif sequence == "30":
        plot_graph(group=sequence, file_name=file[:-4], colour='blue', x_vals=x, y_vals=y)

    elif sequence == "60":
        plot_graph(group=sequence, file_name=file[:-4], colour='red', x_vals=x, y_vals=y)
    else:
        print(f"Different time. Actual time was {sequence}")
