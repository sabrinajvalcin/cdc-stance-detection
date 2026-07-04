import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    df = pd.read_csv('./data/all_replies.csv')

    unlabeled_replies, replies_to_label = train_test_split(df, test_size=0.2, random_state=42)

    unlabeled_replies.to_csv('./data/unlabeled_replies.csv', index=False)

    replies_to_label.to_csv('./data/replies_to_label.csv', index=False)