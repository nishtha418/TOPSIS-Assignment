import pandas as pd
import numpy as np
import os

def topsis(input_file, weights, impacts, output_file):

    if not os.path.isfile(input_file):
        raise FileNotFoundError("Input file not found")

    df = pd.read_csv(input_file)

    if df.shape[1] < 3:
        raise ValueError("Input file must contain at least 3 columns")

    data = df.iloc[:, 1:]
    data = data.apply(pd.to_numeric, errors='raise')

    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        raise ValueError("Weights, impacts and criteria count must match")

    if not all(i in ['+', '-'] for i in impacts):
        raise ValueError("Impacts must be + or -")

    norm = data / np.sqrt((data ** 2).sum())
    weighted = norm * weights

    ideal_best, ideal_worst = [], []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    df['Topsis Score'] = score
    df['Rank'] = score.rank(ascending=False).astype(int)

    df.to_csv(output_file, index=False)
