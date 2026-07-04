import pandas as pd
from pathlib import Path 

def generate_file_paths(directory):
    """
    Generate file paths for all cvs in each directory and yield them one by one.

    Parameters:
    directory (Path): The path to the parent directory containing the subdirectories.

    Yields:
    str: The file path of each CSV file found in the directory.
    """
    for file_path in directory.glob("*.csv"):
        yield str(file_path)

def generate_dataframe_from_subdirectory(subdirectory, relevant_columns):
    """
    Generate a DataFrame from all CSV files in a given subdirectory.

    Parameters:
    subdirectory (Path): The path to the subdirectory containing the CSV files.
    relevant_columns (dict): A dictionary specifying the relevant columns to read from the CSV files and their corresponding data types.

    Returns:
    pd.DataFrame: A DataFrame containing the concatenated data from all CSV files in the subdirectory.
    """
    
    file_paths = generate_file_paths(subdirectory)

    df = pd.concat((pd.read_csv(file_path, usecols=relevant_columns.keys(), dtype=relevant_columns) for file_path in file_paths), ignore_index=True)

    df['period'] = subdirectory.name

    return df

def merge_dataframes(subdirectories, relevant_columns):
    """
    Merge DataFrames from all subdirectories into a single DataFrame.

    Parameters:
    subdirectories (list): A list of Path objects representing the subdirectories.
    relevant_columns (dict): A dictionary specifying the relevant columns to read from the CSV files and their corresponding data types.

    Returns:
    pd.DataFrame: A DataFrame containing the concatenated data from all subdirectories.
    """
    merged_df = pd.concat((generate_dataframe_from_subdirectory(subdirectory,relevant_columns) for subdirectory in subdirectories), ignore_index=True)
    merged_df = merged_df.drop_duplicates(subset='id')
    
    #rename 'id' column to comment_id and 'conversation_id to cdc_post_id
    merged_df = merged_df.rename(
        columns={'id': 'comment_id', 'conversation_id': 'cdc_post_id'}
    )

    return merged_df

if __name__ == "__main__":
    
    directory = Path("./data")

    subdirectories = [d for d in directory.iterdir() if d.is_dir()]

    relevant_columns = {
    'id': str,
    'conversation_id': str,
    'created_at': str,
    'text': str,
    'lang': str
    }

    df = merge_dataframes(subdirectories, relevant_columns)

    df.to_csv('./data/all_replies.csv', index=True, index_label='row_id')
