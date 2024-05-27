# %%
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.ticker import MaxNLocator
from typing import List, Dict
import pandas as pd
import numpy as np

# Get the current size
current_size = plt.rcParams["font.size"]


def plot_scores(
    data: List[Dict],
    score_axis_title: str = "10-Fold Cross-Val Mean Accuracy Score [%]",
    path: str = "scores.pdf",
    big_title: str = "",
    if_score: bool = True,
) -> None:

    # Set the new size as a ratio of the current size
    plt.rcParams.update({"font.size": current_size * 1.11})

    # Convert the data into a DataFrame
    df = pd.DataFrame(data)

    # Create a new column for the number of columns in each data point
    df["num_columns"] = df["columns"].apply(len)

    # Plot the mean_score, mean_std, and num_columns
    fig, ax1 = plt.subplots()

    # Plotting for validation scores
    color = "blue"
    ax1.set_xlabel("Nr Iteracji Metody", color="black")
    ax1.set_ylabel(score_axis_title, color="blue")
    ax1.plot(df.index, df["mean_score"], color=color, label="Wynik Walidacji")
    # ax1.fill_between(
    #     df.index,
    #     df["mean_score"] - df["mean_std"],
    #     df["mean_score"] + df["mean_std"],
    #     color=color,
    #     alpha=0.1,
    # )

    # Plotting for training scores
    # color = "green"
    # ax1.plot(df.index, df["train_score"], color=color, label="Training Score")
    # ax1.fill_between(
    #     df.index,
    #     df["train_score"] - df["train_std"],
    #     df["train_score"] + df["train_std"],
    #     color=color,
    #     alpha=0.1,
    # )

    ax1.tick_params(axis="y", labelcolor="blue")
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Add lines for min, max and average of mean_score
    starting_score = df["mean_score"].iloc[0]
    best_score = df["mean_score"].max() if if_score else df["mean_score"].min()

    ax1.axhline(starting_score, color="red", linestyle="--")
    ax1.axhline(best_score, color="blue", linestyle="--")

    # Create custom legend handles
    min_handle = mlines.Line2D(
        [],
        [],
        color="red",
        linestyle="--",
        label=f"""{"Wynik" if if_score else "Błąd"} Bez IC ({round(starting_score, 4)})""",
    )
    max_handle = mlines.Line2D(
        [],
        [],
        color="blue",
        linestyle="--",
        label=f"""{"Najwyższy Wynik" if if_score else "Najniższy Błąd"}({round(best_score, 4)})""",
    )

    # Find the index of the max mean_score
    best_score_index = (
        df["mean_score"].idxmax() if if_score else df["mean_score"].idxmin()
    )

    # Add a vertical line at the position of the max mean_score
    ax1.axvline(best_score_index, color="orange", linestyle="--")

    # Create a custom legend handle for the max value line
    max_value_handle = mlines.Line2D(
        [],
        [],
        color="orange",
        linestyle="--",
        label=f"Najlepsza Iteracja ({best_score_index})",
    )

    # Force x axis to only show integer values
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Replace 0 on x-axis with "No FE"
    labels = [item.get_text() for item in ax1.get_xticklabels()]
    labels[labels.index("0")] = "Bez IC"
    ax1.set_xticklabels(labels)

    # Add the new handle to the legend
    ax1.legend(
        handles=[
            min_handle,
            max_handle,
            max_value_handle,
            # validation_handle,
            # training_handle,
        ],
        loc="best",
    )

    # Create a secondary y-axis for num_columns
    ax2 = ax1.twinx()
    ax2.set_ylabel(
        "Całkowita Liczba Kolumn",
        color="purple",
    )
    ax2.plot(df.index, df["num_columns"], color="purple", alpha=0.5)
    ax2.tick_params(axis="y", labelcolor="purple")
    plt.title(big_title)

    fig.tight_layout()

    # Save the plot as pdf file
    plt.savefig(path)


def plot_columns(
    data: list,
    problem_type: str,
    title: str = "Columns Across Iterations",
    save_path: str = "columns.pdf",
    column_threshold: int = 0,
) -> Dict[int, str]:

    # Set the new size as a ratio of the current size
    plt.rcParams.update({"font.size": current_size * 1.66})

    # Get the unique columns across all iterations and their first appearance
    columns = {}
    for i, d in enumerate(data):
        for col in d["columns"]:
            if col == "target":
                continue
            if col not in columns:
                columns[col] = i

    # Sort the columns by their first appearance
    columns = sorted(columns, key=columns.get)

    # Create a binary matrix indicating the presence of each column in each iteration
    matrix = [[col in d["columns"] for col in columns] for d in data]

    # Transpose the matrix
    matrix = np.transpose(matrix)

    fig, ax = plt.subplots()

    # Extract the mean scores from the data
    scores = [d["mean_score"] for d in data]

    # Find the index of the best score
    if problem_type == "regression":
        best_iter = np.argmin(scores)
    elif problem_type == "classification":
        best_iter = np.argmax(scores)

    # Draw a vertical line at the position of the best iteration
    plt.axvline(x=best_iter, color="blue", linestyle="--")

    # Iterate over each data point in the matrix
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            # If the value is True, plot a square at this position
            # If this is the best iteration, color the square red
            color = "red" if j == best_iter else "black"
            if val:
                ax.scatter(j, i, color=color, s=20, marker="s")

    # Add a title to the plot
    plt.title(title)

    # Add labels to the x and y axes
    plt.xlabel("Nr Iteracji Metody")
    plt.ylabel(f"Kwadraty to unikalne cechy\n sortowane wg 1. wystąpienia")

    # Now the x-axis labels should be the iteration number
    plt.xticks(range(len(data)), range(0, len(data)))

    yticks_content = (
        columns if len(columns) <= column_threshold else range(len(columns))
    )

    # And the y-axis labels should be the unique columns, rotated
    plt.yticks(range(len(columns)), yticks_content, rotation="horizontal")

    # Force x axis to only show integer values
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Replace 0 on x-axis with "No FE"
    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[labels.index("0")] = "Bez IC"
    ax.set_xticklabels(labels)

    # Add a grid to the plot
    plt.grid(True, which="both", color="grey", linewidth=0.3, linestyle="--")

    plt.yticks([])

    plt.tight_layout()

    # Save as pdf
    plt.savefig(save_path)

    # Create a dictionary to map the column index to the column name
    column_mapping = {i: col for i, col in enumerate(columns)}

    return column_mapping


def plot_time(data: List[Dict], path: str = "time.pdf", title: str = "") -> None:
    # Set the new size as a ratio of the current size
    plt.rcParams.update({"font.size": current_size * 1.66})

    # Convert the data into a DataFrame and skip the first row
    df = pd.DataFrame(data)[1:]

    # Calculate the cumulative sum of the time
    df["cumulative_time"] = df["time"].cumsum()

    # Create a figure with two subplots
    fig, ax1 = plt.subplots()

    # Plot the time for each iteration as a line plot with dots on the first subplot
    ax1.plot(
        df.index,
        df["time"],
        marker="o",
        linestyle="-",
        color="royalblue",
    )
    ax1.set_xlabel(
        "Nr Iteracji Metody",
    )
    ax1.set_ylabel(
        "Czas Iteracji [s]",
        color="blue",
    )

    # Calculate the mean and standard deviation of the time
    mean_time = df["time"].mean()
    std_time = df["time"].std()

    # Plot the average time as a horizontal line
    ax1.axhline(mean_time, color="blue", linestyle="--", label="Średni Czas Iteracji")

    # Fill the area between mean_time - std_time and mean_time + std_time
    # ax1.fill_between(
    #     df.index, mean_time - std_time, mean_time + std_time, color="blue", alpha=0.1
    # )

    # Force x axis to only show integer values
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Create a second subplot that shares the same x-axis
    ax2 = ax1.twinx()

    # Plot the cumulative time as a line plot on the second subplot
    ax2.plot(
        df.index,
        df["cumulative_time"],
        color="r",
        marker="o",
        linestyle="-",
    )
    ax2.set_ylabel(
        "Skumulowany Czas Iteracji [s]",
        color="red",
    )

    # Add a legend to each subplot
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")

    # Change the color of the axes
    ax1.spines["left"].set_color("blue")
    ax2.spines["right"].set_color("red")

    # Change the color of the ticks
    ax1.tick_params(axis="y", colors="blue")
    ax2.tick_params(axis="y", colors="red")

    plt.title(title)

    plt.tight_layout()

    # Save the plot as a pdf file
    plt.savefig(path)


# %%
def calculate_model_stats(file_path, groupby="machine_learning_model"):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Add type of problem depending on model name. If it contains 'regression', it is a regression problem.
    df["problem_type"] = df["machine_learning_model"].apply(
        lambda x: "cls" if "Classifier" in x else "reg"
    )

    # Group by 'machine_learning_model'
    grouped = df.groupby(groupby)

    # Calculate statistics for each group
    stats = grouped.agg(
        {
            "experiment_no": "count",
            "problem_type": "first",
            "best_score_%": lambda x: x[df["whether_improved"] == True].mean(),
            "initial_score_%": lambda x: x[df["whether_improved"] == True].mean(),
            "percentage_change_%": lambda x: x[df["whether_improved"] == True].mean(),
            "whether_improved": lambda x: x.sum()
            / len(x)
            * 100,  # percentage of True values
        }
    )

    # Rename columns for clarity
    stats.rename(
        columns={
            "experiment_no": "experiment_count",
            "best_score_%": "average_best_metric",
            "initial_score_%": "average_initial_metric",
            "percentage_change_%": "average_percentage_change_%",
            "whether_improved": "improvement_rate_%",
        },
        inplace=True,
    )

    # Sort the DataFrame by absolute value of 'average_percentage_change_%'
    # by abs
    stats = stats.reindex(
        stats["average_percentage_change_%"].abs().sort_values(ascending=False).index
    )

    return stats.round(2)


# %%
# calculate_model_stats("scores.csv", groupby="machine_learning_model")
# # %%
# calculate_model_stats("scores.csv", groupby="dataset_name")
# # %%
# calculate_model_stats("scores.csv", groupby="problem_type")
# # %%
# df = pd.read_csv("scores.csv")
# %%
# %%
# import pandas as pd

# df = pd.read_csv("caafe.csv")
# df["GAIN_PERC_3_5"] = (df.CAAFE_GPT_3_5 - df.No_FE) / df.No_FE * 100
# df["GAIN_PERC_4"] = (df.CAAFE_GPT_4 - df.No_FE) / df.No_FE * 100
# df.round(2).sort_values("GAIN_PERC_4", ascending=False)
# %%
