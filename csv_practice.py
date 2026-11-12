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

print("--- Exercise 4 ---")

total_revenue = 0

with open(file_path, "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total  # adds each sale to the total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

print("--- Exercise 5 ---")

original_count = 0
written_count = 0

with open(file_path, "r") as input_file, open("data/cleaned.csv", "w", newline="") as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    header = next(reader)

    writer.writerow(["Product", "Price", "Qty", "Total"])

    for row in reader:
        original_count += 1

        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity

        if total > 100:  # only keep sales over $100
            writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
            written_count += 1

print(f"Rows written: {written_count}")
print(f"Original rows: {original_count}")
