# Template for loading a txt file from your laptop

import pandas as pd
import os

# ============================================
# OPTION 1: If your txt file is structured data (like CSV/TSV)
# ============================================

# Set the path to your txt file
# Use absolute path: '/Users/evelynhuang/Documents/myfile.txt'
# Or relative path: 'data/myfile.txt'
file_path = "/Users/evelynhuang/Downloads/influencers.txt"

# Load as DataFrame (if it's tabular/structured data)
# For tab-separated values:
df = pd.read_csv(file_path, sep='\t')

# For comma-separated values:
# df = pd.read_csv(file_path, sep=',')

# For space-separated values:
# df = pd.read_csv(file_path, sep=' ')

# For any delimiter (pandas will try to detect):
# df = pd.read_table(file_path)

# ============================================
# OPTION 2: If your txt file is plain text
# ============================================

# Read entire file as string
# with open(file_path, 'r') as f:
#     content = f.read()

# Read line by line into a list
# with open(file_path, 'r') as f:
#     lines = f.readlines()

# Read as list of lines (without newline characters)
# with open(file_path, 'r') as f:
#     lines = [line.strip() for line in f]

# ============================================
# Basic exploration (if using DataFrame)
# ============================================

# Clean up: Remove rows that are separator lines (if any)
df = df[~df['Username'].str.contains('=', na=False)]

print("First 5 records:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())

print("\nSample data:")
print(df.head(10))

