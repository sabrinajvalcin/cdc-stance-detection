import re
import pandas as pd


def remove_missing_and_duplicates(df, text_column="text"):
    df = df.dropna(subset=[text_column])
    df = df.drop_duplicates(subset=[text_column])
    return df


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def clean_comments_dataframe(df, text_column="text"):
    df = remove_missing_and_duplicates(df, text_column)
    df["clean_text"] = df[text_column].apply(clean_text)
    return df