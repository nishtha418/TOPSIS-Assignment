import sys
from topsis.topsis import run_topsis

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage:")
        print("python -m topsis <InputDataFile> <Weights> <Impacts> <OutputFileName>")
        sys.exit(1)

    run_topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
