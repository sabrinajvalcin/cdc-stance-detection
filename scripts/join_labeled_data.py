import pandas as pd
from pathlib import Path
import os

if __name__ == "__main__":
    print(os.getcwd())

    labels_path = Path('./data/complete_CDC_labels.xlsx')
    replies_path = Path('./data/replies_to_label.csv')
   
    labels_df = pd.read_excel(labels_path, usecols=['row_id', 'label'])
    replies_df = pd.read_csv(replies_path)

    # perform left join on the two dataframes based on the 'row_id' column
    merged_df = pd.merge(replies_df, labels_df, on='row_id', how='left')

    # success if merge_df does not contain any null values in the 'label' column
    if merged_df['label'].isnull().sum() == 0:
        print("Merge successful. No null values in 'label' column.")
        merged_df.to_csv('./data/labeled_replies.csv', index=False)
    else:
        print(f"Error: Merge resulted in {merged_df['label'].isnull().sum()} null values in 'label' column.")