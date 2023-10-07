import pandas as pd
import argparse
from typing import List, Dict

def pen_file(path: str) -> List[List[object]]:
    df = pd.read_csv(path)
    return df.values.tolist()

if __name__ == "__main__":
    # Придумываем аргументы которые сможет прочитать прога
    parser = argparse.ArgumentParser(description="our little spotify experience")
    parser.add_argument('file_path', type=str, help="input path to our datasheet")
    parser.add_argument('-v', '--verbose', action="store_true", help="shows more info during script run")

    args = parser.parse_args()

    if args.verbose:
        print(args)
        print("Hello world")
        print(f'File path: {args.file_path}')

    table = pen_file(args.file_path)

    print(len(table))
