from typing import List
import os, json
from vis import plot_scores, plot_time, plot_columns
import numpy as np
import pandas as pd


def extract_scores(src_dir: str) -> List[str]:
    """
    Extracts paths to all `scores.json` files in highest numbered subdirectories of each directory in the source directory.

    Parameters:
    src_dir (str): The source directory containing the directories with the `scores.json` files.

    Returns:
    List[str]: A list of paths to the scores.json files.
    """

    # Get list of directories in source directory
    directories = [
        dir_name
        for dir_name in os.listdir(src_dir)
        if os.path.isdir(os.path.join(src_dir, dir_name))
    ]

    # Initialize list to store paths
    scores_paths = []

    # Iterate over each directory
    for directory in directories:
        # Get list of subdirectories
        subdirectories = [
            sub_dir
            for sub_dir in os.listdir(os.path.join(src_dir, directory))
            if os.path.isdir(os.path.join(src_dir, directory, sub_dir))
        ]

        # Skip if no subdirectories
        if not subdirectories:
            continue

        # Get subdirectory with highest number as name
        max_subdirectory = max(
            subdirectories,
            key=lambda x: (
                int(x) if os.path.isfile(os.path.join(x, "scores.json")) else -1
            ),
        )

        # Assemble path to scores.json file
        scores_path = os.path.join(src_dir, directory, max_subdirectory, "scores.json")

        # Check if file exists
        if not os.path.exists(scores_path):
            continue

        # Add path to list
        scores_paths.append(scores_path)

    return scores_paths


if __name__ == "__main__":
    scores_paths = extract_scores(
        src_dir=r"C:\Users\matlaczj\Documents\Repozytoria\AutoFEASULMs\archive\logs-9"
    )
    image_path = r"C:\Users\matlaczj\Documents\Repozytoria\AutoFEASULMs\src\vis\images"

    n_improved = 0
    for path in scores_paths:
        with open(
            path,
            "r",
        ) as file:
            data = json.load(file)

        title = path.split("\\")[-3]
        problem_type = "regression" if "REGRES" in title else "classification"

        if title != "0-MISTRAL-AUTOPRICE-RIDGE_REGRESSION":
            continue

        df = pd.DataFrame(data)
        best_iteration = (
            df["mean_score"].idxmax()
            if problem_type == "classification"
            else df["mean_score"].idxmin()
        )
        x = df.loc[0, "mean_score"]
        y = df.loc[best_iteration, "mean_score"]
        r = y / x
        percentage_change = r - 1
        print(f"{title}: {percentage_change:.2f}")
        if (problem_type == "classification" and percentage_change > 0) or (
            problem_type == "regression" and percentage_change < 0
        ):
            n_improved += 1

        plot_scores(
            data=data,
            big_title=title,
            if_score=True if problem_type == "classification" else False,
            score_axis_title=(
                f"""10-Fold Cross-Val Mean {'Accuracy Score' if problem_type == "classification" else 'MAPE Error'}"""
            ),
            path=f"{image_path}\{title}_scores.svg",
        )

        plot_time(data=data, title=title, path=f"{image_path}\{title}_time.svg")

        plot_columns(
            data=data,
            problem_type=problem_type,
            title=title,
            save_path=f"{image_path}\{title}_columns.svg",
        )
    print(
        f"Improved: {n_improved}/{len(scores_paths)} ({n_improved/len(scores_paths)*100:.2f}%)"
    )
