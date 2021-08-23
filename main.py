from dataclasses import dataclass
from typing import List, Optional

import pandas as pd




if __name__ == '__main__':
    df = pd.read_csv('publications_min.csv', index_col=0)
    authors = df['authors'].dropna()
    for a in authors.to_list():
        print(a)