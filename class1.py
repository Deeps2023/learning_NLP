import pandas as pd
import scanpy as sc

from datasets import load_dataset

# Load all splits of the dataset
dataset = load_dataset("dair-ai/emotion")

# Access train, test, or validation split
train_data = dataset["train"]
test_data = dataset["test"]

# Display an example from the train split
print(train_data[0])
