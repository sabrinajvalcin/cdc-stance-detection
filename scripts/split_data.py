import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    df = pd.read_csv('./data/merged_data_all_periods.csv')

    X_train, X_test = train_test_split(df, test_size=0.2, random_state=42)

    X_train.to_csv('./data/train_data.csv', index=False)
    
    X_test.to_csv('./data/test_data_unlabeled.csv', index=False)