import pandas as pd
from pathlib import Path


def merge_comment_files(input_folder, total_files=12, text_column="text"):
    input_folder = Path(input_folder)
    comments = []

    for i in range(1, total_files + 1):
        file_path = input_folder / f"{i}.csv"
        df = pd.read_csv(file_path)
        comments.append(df[[text_column]])

    all_comments = pd.concat(comments, ignore_index=True)

    return all_comments


def save_dataframe(df, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")