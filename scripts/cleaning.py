import re
import pandas as pd


def keep_text_column(df, text_column="text"):
    """
    Keeps only the text column from the dataframe.
    """
    return df[[text_column]].copy()


def remove_missing_and_duplicates(df, text_column="text"):
    """
    Removes missing values and duplicate comments.
    """
    df = df.dropna(subset=[text_column])
    df = df.drop_duplicates(subset=[text_column])
    return df.copy()


def clean_text(text):
    """
    Cleans a single text comment.
    """
    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove mentions such as @CDCgov, @WHO, @user
    text = re.sub(r"@\w+", "", text)

    # Remove hashtag symbol but keep the word
    text = re.sub(r"#", "", text)

    # Remove non-letter characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def clean_comments_dataframe(df, text_column="text"):
    """
    Keeps only the text column, removes missing values and duplicates,
    and creates a clean_text column.
    """
    df = keep_text_column(df, text_column)
    df = remove_missing_and_duplicates(df, text_column)
    df["clean_text"] = df[text_column].apply(clean_text)
    return df