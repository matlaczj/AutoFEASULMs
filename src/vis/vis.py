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
    """
    Function to plot mean_score, mean_std, and num_columns.

    Parameters:
    data (List[Dict]): A list of dictionaries containing 'mean_score', 'mean_std', and 'columns'.

    Returns:
    None
    """
    # Convert the data into a DataFrame
    df = pd.DataFrame(data)

    # Create a new column for the number of columns in each data point
    df["num_columns"] = df["columns"].apply(len)

    # Plot the mean_score, mean_std, and num_columns
    fig, ax1 = plt.subplots()

    color = "tab:blue"
    ax1.set_xlabel("Method's Iteration")
    ax1.set_ylabel(score_axis_title, color=color)
    ax1.plot(df.index, df["mean_score"], color=color)
    ax1.fill_between(
        df.index,
        df["mean_score"] - df["mean_std"],
        df["mean_score"] + df["mean_std"],
        color=color,
        alpha=0.1,
    )
    ax1.tick_params(axis="y", labelcolor=color)
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Add lines for min, max and average of mean_score
    starting_score = df["mean_score"].iloc[0]
    best_score = df["mean_score"].max() if if_score else df["mean_score"].min()
    avg_score = df["mean_score"].mean()

    min_line = ax1.axhline(starting_score, color="red", linestyle="--")
    max_line = ax1.axhline(best_score, color="green", linestyle="--")
    avg_line = ax1.axhline(avg_score, color="purple", linestyle="--")

    # Define an offset for the x-coordinate of the text annotation
    offset = 0.02 * len(df.index) * 4

    # Add text for min, max and average of mean_score
    ax1.text(
        0,
        starting_score,
        f"{round(starting_score,2)}",
        color="red",
        va="bottom",
        ha="left",
    )
    ax1.text(
        offset,  # Add the offset to the x-coordinate
        best_score,
        f"{round(best_score,2)}",
        color="green",
        va="bottom",
        ha="left",
    )
    ax1.text(
        2 * offset,  # Add twice the offset to the x-coordinate
        avg_score,
        f"{round(avg_score,2)}",
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

    # Add the new handle to the legend
    ax1.legend(handles=[min_handle, max_handle, avg_handle, max_value_handle])

    # Create a secondary y-axis for num_columns
    ax2 = ax1.twinx()
    ax2.set_ylabel("Total Number of Columns", color="tab:gray")
    ax2.plot(df.index, df["num_columns"], color="tab:gray", alpha=0.6)
    ax2.tick_params(axis="y", labelcolor="tab:gray")
    plt.title(big_title)

    fig.tight_layout()

    # Save the plot as pdf file
    plt.savefig(path)


def plot_columns(
    data: list,
    problem_type: str,
    title: str = "Columns Across Iterations",
    fig_size: tuple = None,
    font_size: int = 12,
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

    # Calculate the figure size based on the number of iterations and columns if not provided
    if fig_size is None:
        fig_size = (max(8, len(data) // 2), max(8, len(columns) // 2))

    # Increase the figure size
    fig, ax = plt.subplots(figsize=fig_size)

    # Increase the font size
    mpl.rcParams["font.size"] = font_size

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
                ax.scatter(j, i, color=color, s=200, marker="s")

    # Add a title to the plot
    plt.title(title, pad=16)

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

    # Adjust the spacing between the labels and the plot
    plt.subplots_adjust(bottom=0.15)

    # Add padding between y-axis labels and the axis
    ax.tick_params(axis="y", which="major", pad=10)

    # Add a grid to the plot
    plt.grid(True, which="both", color="grey", linewidth=0.5, linestyle="--")

    # Save as pdf
    plt.savefig(save_path, bbox_inches="tight")

    return column_mapping
