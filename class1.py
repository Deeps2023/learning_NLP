import pandas as pd
import scanpy as sc
import pandas as pd
import matplotlib.pyplot as plt

from datasets import load_dataset

# Load all splits of the dataset
dataset = load_dataset("dair-ai/emotion")

# Access train, test, or validation split
train_data = dataset["train"]
test_data = dataset["test"]

# Display an example from the train split
print(train_data[0])

#eda
print(dataset)

import matplotlib.pyplot as plt

# Extract labels from the training dataset
labels = [example['label'] for example in dataset['train']]

# Count label occurrences
from collections import Counter
label_counts = Counter(labels)

# Plot the label distribution
plt.bar(label_counts.keys(), label_counts.values())
plt.xticks([0,1,2,3,4,5], ['sadness', 'joy','love','anger','fear','surprise'])
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Label Distribution in Training Set')
plt.show()
