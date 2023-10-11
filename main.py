import pandas as pd
import argparse
from typing import List


def open_file(file_path: str) -> List[List[object]]:
    df = pd.read_csv(file_path)
    return df


def get_year_stats(sheet: List) -> pd.Series:
    return sheet.groupby(['year'])['track_id'].count().to_string()


def get_top_artist_count(sheet, n=5) -> pd.Series:
    return sheet.groupby(['artist_name'])['track_id'].count().sort_values(ascending=False)[:n].to_string()


if __name__ == "__main__":
    # Придумываем аргументы которые сможет прочитать прога
    parser = argparse.ArgumentParser(description="our little spotify experience")
    parser.add_argument('file_path', type=str, help="input path to our datasheet")
    parser.add_argument('-v', '--verbose', action="store_true", help="shows more info during script run")
    parser.add_argument("-len", "--length_of_table", action="store_true", help="returns length of the table")
    parser.add_argument("-t", "--top_artists", type=int, help="returns top artists")
    parser.add_argument("-s", "--stats", action="store_true", help="returns year stats")

    args = parser.parse_args()

    if args.verbose:
        print(args)
        print("Hello world")
        print(f'File path: {args.file_path}')

    table = open_file(args.file_path)
    print()

    if args.length_of_table:
        print("Length of the table:", len(table))
        print()

    if args.stats:
        print('Statistic of years:', get_year_stats(table)[4:])
        print()

    if args.top_artists:
        print('Top artists:', get_top_artist_count(table, args.top_artists)[11:])
        print()
