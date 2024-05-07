from colorama import Fore
from vis.vis import plot_scores, plot_columns, plot_time


def check_early_stopping(k, threshold, problem_type, scores, iteration):
    if iteration >= k:
        last_k_scores = [score["mean_score"] for score in scores[-k:]]
        percentage_changes = [
            (last_k_scores[i + 1] - last_k_scores[i]) / last_k_scores[i]
            for i in range(len(last_k_scores) - 1)
        ]
        if all(
            (
                (change >= threshold)
                if problem_type == "regression"
                else (change <= -threshold)
            )
            for change in percentage_changes
        ):
            print(f"{Fore.RED}Early stopping mechanism triggered.{Fore.RESET}")
            print(f"{Fore.RED}Reason 1: {last_k_scores}{Fore.RESET}")
            print(f"{Fore.RED}Reason 2: {percentage_changes}{Fore.RESET}\n")
            return True
    return False


def plot_experiment_results(
    dataset_name, model_name, problem_type, validation_kfold, scores, iter_base
):
    title = (
        f"""Results In Each Iteration\nDataset: {dataset_name} ML Model: {model_name}"""
    )
    plot_scores(
        scores,
        big_title=title,
        score_axis_title=(
            f"""{validation_kfold}-Fold Cross-Val Mean {'Accuracy Score' if problem_type == "classification" else 'MAPE Error'}"""
        ),
        path=iter_base + "scores.pdf",
        if_score=(True if problem_type == "classification" else False),
    )

    title = f"""Column Creation And Selection History\nDataset: {dataset_name} ML Model: {model_name}"""
    plot_columns(
        data=scores,
        title=title,
        save_path=iter_base + "columns.pdf",
        problem_type=problem_type,
    )

    title = f"""Time Of Execution For Each Iteration\nDataset: {dataset_name} ML Model: {model_name}"""
    plot_time(
        data=scores,
        path=iter_base + "time.pdf",
        title=title,
    )
