import pandas as pd
import os

# Define input and output file paths
input_file = "/Users/ashish/Desktop/pbl_hairloss/train_ds_woaug.csv"

df = pd.read_csv(input_file)
df["original_column"] = df["path"]




# Define prefixes
prefixes = ['clahe_', 'blurred_', 'noisy_', 'crop_', 'flipped_']
rows = []
for _, row in df.iterrows():
    for prefix in prefixes:
        new_row = row.copy()
        new_row["column_name"] = prefix + row["path"]
        rows.append(new_row)

# Create a new DataFrame with the expanded rows
new_df = pd.DataFrame(rows)

# Write the new DataFrame to a CSV file
if not os.path.exists("/Users/ashish/Desktop/pbl_hairloss/train_ds_aug3.csv"):
    new_df.to_csv("/Users/ashish/Desktop/pbl_hairloss/train_ds_aug3.csv", index=False)
else:
    new_df.to_csv("/Users/ashish/Desktop/pbl_hairloss/train_ds_aug3.csv", mode="a", header=False, index=False)