import ast

import pandas as pd
from tqdm import tqdm

from src.author import Author


if __name__ == '__main__':
    df = pd.read_csv('publications_min.csv', index_col=0)
    authors = df['authors'].dropna()

    full = []
    partial = []
    zero = []

    # TODO: - Better handling of 'von', 'de', etc.
    for author_list in authors.to_list():
        author_list_purged = author_list.replace(".", " ").replace(" -", " ").replace("  ", " ")
        for author_text in ast.literal_eval(author_list_purged):
            author = Author.from_string(author_text)
            if author.full_prct() == 1.0:
                full.append(author)
            elif author.full_prct() > 0.0:
                partial.append(author)
            else:
                zero.append(author)

    full_authors = set(full)
    incomplete_authors = set()

    # TODO: - Efficiency - complexity too high - brute force
    for author in tqdm(set(partial + zero)):
        matching_authors = filter(lambda a: len(a.names) == len(author.names) and a.last_name == author.last_name, full_authors)
        # TODO: - Better matching
        for match_candidate in matching_authors:
            if match_candidate.similar_prct(author) == 1.0:
                pass
            else:
                incomplete_authors.union(set(matching_authors))

    # TODO: - Capitalize 2nd part of double name eg. 'Hans-jorg'
    return_df = pd.DataFrame([a.dict() for a in full_authors.union(incomplete_authors)])
    return_df.to_csv('unique_people.csv', index=False)
