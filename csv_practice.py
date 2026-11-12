# csv_practice.py
# Author: Randall McKendry
# Module 12 Lab: Read a Sales CSV, Write a Cleaned Report

import csv
from datetime import datetime

print("--- Exercise 1 ---")

file_path = "data/sales.csv" #where the file is

print("---Exercise 2 ---")

with open(file_path, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

print("---Exercise 3 ---")

with open(file_path, "r") as file:
    reader = csv.reader(file)

    header = next(reader)  # Skip the header row
    print("Header:", header)

    for row in reader:
        print(row)

