# R(i,j) Matrix Min-Max Range Checker

This project provides a Python script that processes a numerical dataset, computes an `R(i,j)` matrix, and checks if the values of a randomly generated object fall within the min and max range of each column in the matrix. If any value does not lie within the specified range, it will return the name of the columns where the mismatch occurs. Additionally, a visualization is provided for mismatched columns.

## Features

- **Dataset Handling**: Loads an Excel file (`.xlsx`) and selects numerical columns.
- **R(i,j) Matrix Calculation**: Computes an `R(i,j)` matrix based on relationships between column values.
- **Min-Max Range Checking**: Generates a random object and checks if the `R(i,j)` values for this object fall within the precomputed min and max ranges for each column.
- **Visualization**: Displays a bar chart showing the min and max values for columns where the random object's values did not fit within the expected range.

## Requirements

To run the script, you need Python 3.x and the following dependencies:

- pandas
- numpy
- matplotlib
- openpyxl (for reading `.xlsx` files)

### Installation

To install the required dependencies, run the following command in your terminal:

```bash
pip install pandas numpy matplotlib openpyxl
