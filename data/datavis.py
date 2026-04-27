import pyarrow.parquet as pq
import pandas as pd

# Read the parquet file
df = pd.read_parquet("demo_1000.parquet")

print(df.shape)       # (1000, 120)
print(df.head(10))     # ['user_id', 'item_id', 'label_type', ...]
df.head(100).to_csv("demo_1000_first100.csv", index=False)
# from datasets import load_dataset

# ds = load_dataset("TAAC2026/data_sample_1000")
# print(ds)