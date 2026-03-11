import pandas as pd

def add_feature(fname):
    df = pd.read_csv('data/sample_dataset.csv')
    new_feature_df = pd.read_csv(fname)
    new_feature_df["name"] = new_feature_df["name"].str.lower()

    df_merged = pd.merge(df, new_feature_df, on="name")

    df_columns = df.columns.tolist()[:-1]
    new_feature_df_columns = new_feature_df.columns.tolist()[1:]
    new_columns = df_columns + new_feature_df_columns
    new_columns.append("label")

    df_merged = df_merged.reindex(columns=new_columns)
    df_merged.to_csv('data/sample_dataset_new.csv', index=False)
    

def main():
    add_feature("data/sample_data_pharmacodynamics.csv")

main()