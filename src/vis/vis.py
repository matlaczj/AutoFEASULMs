# %%
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.ticker import MaxNLocator
import matplotlib as mpl
from typing import List, Dict
import pandas as pd
import numpy as np


def plot_scores(
    data: List[Dict],
    score_axis_title: str = "10-Fold Cross-Val Accuracy Score [%] With Std Dev",
    path: str = "scores.pdf",
    big_title: str = "",
    if_score: bool = True,
) -> None:
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)

    # Create a new column for the number of columns in each data point
    df["num_columns"] = df["columns"].apply(len)

    # Plot the mean_score, mean_std, and num_columns
    fig, ax1 = plt.subplots()

    color = "blue"
    ax1.set_xlabel("Method's Iteration", color="black")
    ax1.set_ylabel(score_axis_title, color=color)
    ax1.plot(df.index, df["mean_score"], color=color)
    ax1.fill_between(
        df.index,
        df["mean_score"] - df["mean_std"],
        df["mean_score"] + df["mean_std"],
        color=color,
        alpha=0.3,
    )
    ax1.tick_params(axis="y", labelcolor=color)
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Add lines for min, max and average of mean_score
    starting_score = df["mean_score"].iloc[0]
    best_score = df["mean_score"].max() if if_score else df["mean_score"].min()
    avg_score = df["mean_score"].mean()

    ax1.axhline(starting_score, color="red", linestyle="--")
    ax1.axhline(best_score, color="green", linestyle="--")
    ax1.axhline(avg_score, color="purple", linestyle="--")

    # Define an offset for the x-coordinate of the text annotation
    offset = 0.02 * len(df.index) * 6

    # Add text for min, max and average of mean_score
    ax1.text(
        0,
        starting_score,
        f"{round(starting_score, 4)}",
        color="red",
        va="bottom",
        ha="left",
    )
    ax1.text(
        offset,  # Add the offset to the x-coordinate
        best_score,
        f"{round(best_score, 4)}",
        color="green",
        va="bottom",
        ha="left",
    )
    ax1.text(
        2 * offset,  # Add twice the offset to the x-coordinate
        avg_score,
        f"{round(avg_score, 4)}",
        color="purple",
        va="bottom",
        ha="left",
    )

    # Create custom legend handles
    min_handle = mlines.Line2D(
        [],
        [],
        color="red",
        linestyle="--",
        label=f"""No FE {"Score" if if_score else "Error"}""",
    )
    max_handle = mlines.Line2D(
        [],
        [],
        color="green",
        linestyle="--",
        label=f"""{"Highest Score" if if_score else "Smallest Error"}""",
    )
    avg_handle = mlines.Line2D(
        [],
        [],
        color="purple",
        linestyle="--",
        label=f"""Avg {"Score" if if_score else "Error"}""",
    )

    # Find the index of the max mean_score
    best_score_index = (
        df["mean_score"].idxmax() if if_score else df["mean_score"].idxmin()
    )

    # Add a vertical line at the position of the max mean_score
    ax1.axvline(best_score_index, color="orange", linestyle="--")

    # Create a custom legend handle for the max value line
    max_value_handle = mlines.Line2D(
        [], [], color="orange", linestyle="--", label="Best Iteration"
    )

    # Force x axis to only show integer values
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Replace 0 on x-axis with "No FE"
    labels = [item.get_text() for item in ax1.get_xticklabels()]
    labels[labels.index("0")] = "No Feature\nEngineering"
    ax1.set_xticklabels(labels)

    # Add the new handle to the legend
    ax1.legend(handles=[min_handle, max_handle, avg_handle, max_value_handle])

    # Create a secondary y-axis for num_columns
    ax2 = ax1.twinx()
    ax2.set_ylabel(
        "Total Number of Columns",
        color="black",
    )
    ax2.plot(df.index, df["num_columns"], color="tab:gray", alpha=1)
    ax2.tick_params(axis="y", labelcolor="black")
    plt.title(big_title)

    fig.tight_layout()

    # Save the plot as pdf file
    plt.savefig(path)


def plot_columns(
    data: list,
    problem_type: str,
    title: str = "Columns Across Iterations",
    save_path: str = "columns.pdf",
    column_threshold: int = 10,
) -> Dict[int, str]:

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

    # Increase the figure size
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
    plt.xlabel("Method's Iteration")
    plt.ylabel("Column ID")

    # Now the x-axis labels should be the iteration number
    plt.xticks(range(len(data)), range(0, len(data)))

    yticks_content = (
        columns if len(columns) <= column_threshold else range(len(columns))
    )

    # Create a dictionary to map the column index to the column name
    column_mapping = {i: col for i, col in enumerate(columns)}

    # And the y-axis labels should be the unique columns, rotated
    plt.yticks(range(len(columns)), yticks_content, rotation="horizontal")

    # Force x axis to only show integer values
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Replace 0 on x-axis with "No FE"
    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[labels.index("0")] = "No Feature\nEngineering"
    ax.set_xticklabels(labels)

    # Add a grid to the plot
    plt.grid(True, which="both", color="grey", linewidth=0.3, linestyle="--")

    plt.tight_layout()

    # Save as pdf
    plt.savefig(save_path)

    return column_mapping


def plot_time(data: List[Dict], path: str = "time.pdf", title: str = "") -> None:
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
        label="Time Per Iteration",
    )
    ax1.set_xlabel(
        "Method's Iteration",
    )
    ax1.set_ylabel(
        "Time Taken [s]",
        color="blue",
    )
    mean_time = df["time"].iloc[1:].mean()
    ax1.axhline(mean_time, color="blue", linestyle="--", label="Average Time")

    # Force x axis to only show integer values
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Create a second subplot that shares the same x-axis
    ax2 = ax1.twinx()

    # Plot the cumulative time as a line plot on the second subplot
    ax2.plot(
        df.index,
        df["cumulative_time"],
        color="r",
        label="Cumulative Time",
        marker="o",
        linestyle="-",
    )
    ax2.set_ylabel(
        "Cumulative Time Taken [s]",
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
# import json

# with open(
#     r"C:\Users\matlaczj\Documents\Repozytoria\AutoFEASULMs\archive\logs-8-GOAT\27-MISTRAL-LETTER-GAUSSIAN_NAIVE_BAYES_CLASSIFIER\10\scores.json",
#     "r",
# ) as f:
#     data = json.load(f)
# # %%
# plot_columns(data, "regression", title="Linear Regression\nHouse Prices")
# # %%
# plot_scores(
#     data,
#     big_title="Linear Regression\nHouse Prices",
# )
# # %%
# plot_time(data, title="Linear Regression\nHouse Prices")
# %%
