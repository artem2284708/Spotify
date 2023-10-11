import pandas as pd
import argparse
from typing import List, Dict
def open_file(file_path: str) -> List[List[object]]:
    df = pd.read_csv(file_path)
    return df

def get_year_stats(table: List) -> Dict:
    stat = pd.DataFrame(table)
    return stat.groupby(['year'])['track_id'].count()

def get_top_artist_count(table, n=5):
    artists = dict()
    for row in table:
        artists[row[7]] = artists.get(row[7], 0) + 1
    return sorted(artists.items(), key=lambda x: x[1], reverse=True)[:n]
if __name__ == "__main__":
    # Придумываем аргументы которые сможет прочитать прога
    parser = argparse.ArgumentParser(description="our little spotify experience")
    parser.add_argument('file_path', type=str, help="input path to our datasheet")
    parser.add_argument('-v', '--verbose', action="store_true", help="shows more info during script run")
    parser.add_argument("-t", "--top_artists", type=int, help="returns top artists")
    parser.add_argument("-s", "--stats", action="store_true", help="returns year stats")

    args = parser.parse_args()

    if args.verbose:
        print(args)
        print("Hello world")
        print(f'File path: {args.file_path}')

    table = open_file(args.file_path)

    if args.top_artists:
        res = get_top_artist_count(table, args.top_artists)
        for idx, el in enumerate(res):
            print(f"{idx + 1}) {el[0]}: {el[1]}")

    if args.stats:
        print(get_year_stats(table))

    value = table.values.tolist()

    print('length of table:', len(value))
