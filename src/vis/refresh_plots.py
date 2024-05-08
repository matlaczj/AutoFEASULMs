# %%
from typing import List
import os, json
from vis import plot_scores, plot_time, plot_columns
import numpy as np
import pandas as pd
import re


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

    # Sort directories by name by first number in name
    directories = sorted(directories, key=lambda x: int(x.split("-")[0]))

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
                int(x)
                if os.path.isfile(os.path.join(src_dir, directory, x, "scores.json"))
                else -1
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
        src_dir=r"C:\Users\matlaczj\Documents\Repozytoria\AutoFEASULMs\logs"
    )
    image_path = r"C:\Users\matlaczj\Documents\Repozytoria\AutoFEASULMs\src\vis\images"

    records = []
    n_improved = 0
    for path in scores_paths:
        with open(
            path,
            "r",
        ) as file:
            data = json.load(file)

        experiment_path = re.sub(
            "\\\\[0-9]+\\\\scores.json", "\\\\experiment.json", path
        )
        with open(experiment_path, "r") as file:
            experiment = json.load(file)

        dataset_name = experiment["dataset"]["name"]
        machine_learning_model = experiment["problem"]["machine_learning_model"]

        title = path.split("\\")[-3]
        problem_type = "regression" if "REGRES" in title else "classification"

        # if title != "23-MISTRAL-MUSHROOM-GAUSSIAN_NAIVE_BAYES_CLASSIFIER":
        #     continue

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

        record = {
            "experiment_no": int(title.split("-")[0]),
            "dataset_name": dataset_name,
            "machine_learning_model": machine_learning_model,
            "best_iteration": best_iteration,
            "best_score_%": (y * 100).round(2),
            "initial_score_%": (x * 100).round(2),
            "percentage_change_%": (percentage_change * 100).round(2),
            "whether_improved": (
                percentage_change > 0
                if problem_type == "classification"
                else percentage_change < 0
            ),
        }
        records.append(record)

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

    df = pd.DataFrame(records)
    improved_ratio = (df["whether_improved"].sum() / len(df)).round(2)
    mean_improvement = (
        df[df["whether_improved"] == True]["percentage_change_%"].abs().mean().round(2)
    )
    print(f"Percent of improved results: {improved_ratio}")
    print(f"Mean improvement: {mean_improvement}")
    df = df.sort_values(
        by="percentage_change_%", key=lambda x: np.abs(x), ascending=False
    )
    df.to_csv(
        r"C:\Users\matlaczj\Documents\Repozytoria\AutoFEASULMs\src\vis\scores.csv",
        index=False,
    )

# %%


# %%
