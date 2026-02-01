import sys
import pandas as pd
import numpy as np
import os

def run_topsis(input_file, weights, impacts, output_file):


    # ---------- File existence check ----------
    if not os.path.isfile(input_file):
        print("Error: Input file not found.")
        sys.exit(1)

    # ---------- Read input file ----------
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print("Error while reading the input file.")
        sys.exit(1)

    # ---------- Minimum column check ----------
    if df.shape[1] < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)

    # ---------- Separate data ----------
    data = df.iloc[:, 1:]

    # ---------- Numeric check ----------
    try:
        data = data.apply(pd.to_numeric, errors='raise')
    except:
        print("Error: Columns from 2nd to last must contain numeric values only.")
        sys.exit(1)

    # ---------- Parse weights & impacts ----------
    weights = weights.split(',')
    impacts = impacts.split(',')

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        print("Error: Number of weights, impacts, and criteria columns must be same.")
        sys.exit(1)

    try:
        weights = np.array(list(map(float, weights)))
    except:
        print("Error: Weights must be numeric and comma separated.")
        sys.exit(1)

    if not all(i in ['+', '-'] for i in impacts):
        print("Error: Impacts must be either '+' or '-'.")
        sys.exit(1)

    # ---------- Normalization ----------
    norm_data = data / np.sqrt((data ** 2).sum())

    # ---------- Weighted normalization ----------
    weighted_data = norm_data * weights

    # ---------- Ideal best & worst ----------
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_data.iloc[:, i].max())
            ideal_worst.append(weighted_data.iloc[:, i].min())
        else:
            ideal_best.append(weighted_data.iloc[:, i].min())
            ideal_worst.append(weighted_data.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # ---------- Distance calculation ----------
    dist_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    # ---------- TOPSIS score ----------
    score = dist_worst / (dist_best + dist_worst)

    # ---------- Ranking ----------
    df['Topsis Score'] = score
    df['Rank'] = score.rank(ascending=False).astype(int)

    # ---------- Save output ----------
    df.to_csv(output_file, index=False)
    print("TOPSIS calculation completed successfully.")
    print("Output saved to:", output_file)


# ================= MAIN =================
if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage:")
        print("python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)