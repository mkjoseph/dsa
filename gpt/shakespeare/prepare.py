import os
import requests
import tiktoken
import numpy as np

# download the tiny shakespeare dataset
input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
if not os.path.exists(input_file_path):
    data_url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
    with open(input_file_path, 'w') as f:
        f.write(requests.get(data_url).text)

with open(input_file_path, 'r') as f:
    data = f.read()
n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# train.bin has 301,966 tokens
# val.bin has 36,059 tokens



'''
This script performs several tasks, including downloading a dataset, processing it, encoding it, and saving the encoded data.

1. **Import Required Libraries**:
   - `os`: For interacting with the operating system, like file paths.
   - `requests`: To make HTTP requests, here used for downloading data.
   - `tiktoken`: A library for tokenizing text data, specifically with GPT-2's Byte Pair Encoding (BPE).
   - `numpy`: For numerical operations, particularly array manipulations.

2. **Download 'Tiny Shakespeare' Dataset**:
   - Checks if the dataset file (`input.txt`) exists in the script's directory.
   - If not, it downloads the dataset from a URL and saves it as `input.txt`.

3. **Read and Split the Data**:
   - Reads the entire dataset into a string variable `data`.
   - Splits `data` into training (`train_data`) and validation (`val_data`) sets, with 90% for training and 10% for validation.

4. **Encode the Data Using TikToken**:
   - Initializes a GPT-2 BPE encoder.
   - Encodes the training and validation data, converting text into a list of token IDs.

5. **Export Encoded Data to Binary Files**:
   - Converts the list of token IDs into a NumPy array with `dtype=np.uint16`.
   - Saves these arrays to binary files (`train.bin` and `val.bin`) for efficient storage and retrieval.

6. **Output Token Counts**:
   - Prints the number of tokens in the training and validation datasets.

7. **Final Result**:
   - The script reports the token counts in the `train.bin` and `val.bin` files.

This script is useful for preprocessing text data for machine learning models, especially those using GPT-2's encoding scheme.
'''