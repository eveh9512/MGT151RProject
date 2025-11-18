# Template for loading a JSON file from your laptop

import pandas as pd
import json

# ============================================
# OPTION 1: JSON file with array of objects (most common)
# ============================================

# Set the path to your JSON file
file_path = "/User/evelynhuang/Downloads/JSON-Image_files_mapping.txt"

# Load JSON file directly into DataFrame (if it's an array of objects)
df = pd.read_json(file_path)

# ============================================
# OPTION 2: JSON file with nested structure
# ============================================

# If your JSON has nested data, load it first as JSON, then convert
# with open(file_path, 'r') as f:
#     data = json.load(f)
# 
# # If data is a list of dictionaries
# df = pd.json_normalize(data)
# 
# # If data is a dictionary with a key containing the array
# # Example: {"users": [{...}, {...}]}
# # df = pd.json_normalize(data['users'])

# ============================================
# OPTION 3: JSON Lines format (JSONL/NDJSON - one JSON object per line)
# ============================================

# For JSONL files (each line is a separate JSON object)
# df = pd.read_json(file_path, lines=True)

# ============================================
# OPTION 4: JSON file with specific encoding or orientation
# ============================================

# If your JSON is in a different format, you might need:
# df = pd.read_json(file_path, orient='records')  # for array of objects
# df = pd.read_json(file_path, orient='index')     # for index-oriented
# df = pd.read_json(file_path, orient='columns')  # for column-oriented

# ============================================
# Basic exploration
# ============================================

print("First 5 records:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())

