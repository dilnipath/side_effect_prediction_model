"""when wanting to add new features, this takes feature information of each drug and merges it into the pre-existing dataset"""

import pandas as pd

def add_feature(fname):
    df = pd.read_csv('datasets/dataset.csv')
    new_feature_df = pd.read_csv(fname)
    new_feature_df["name"] = new_feature_df["name"].str.lower()

    df_merged = pd.merge(df, new_feature_df, on="name")

    df_columns = df.columns.tolist()[:-1]
    new_feature_df_columns = new_feature_df.columns.tolist()[1:]
    new_columns = df_columns + new_feature_df_columns
    new_columns.append("label")

    df_merged = df_merged.reindex(columns=new_columns)
    df_merged.to_csv('datasets/sample_dataset_new.csv', index=False)
    

def main():
    add_feature("create_multilabel_dataset/data_halflife.csv")

main()