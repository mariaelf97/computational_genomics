#!/usr/bin/env python3

import argparse
import sys


def get_sequence(reference):
    """Code credit Cassidy Robinhold
    https://gitlab.com/LPCDRP/illumina-blindspots.pub
    input = fasta file
    This function is used to read the genome file and remove useless row in the beginning of the file
    that has a ">" with the length of the genome
    """
    seq_str = ""
    with open(reference) as f:
        for line in f:
            if not line.startswith(">"):
                line = line.strip()
                seq_str += line
    return seq_str


def reverse_string(genome):
    """function to create a suffix array
    code credit : https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/
    input = string to find occurrences in
    output = a suffix array
    """
    n = len(genome)
    suffix = [0] * n
    sub_string = [""] * n

    # Mapping string with its index of
    # it's last letter.
    for i in range(n):
        sub_string[i] = genome[i:]

    # Sorting all substrings
    sub_string.sort()

    # Storing all values of map
    # in suffix array.
    for i in range(n):
        suffix[i] = n - len(sub_string[i])
    return suffix


# flake8: noqa: C901
def find_word(array, query, seq, lo=0, hi=None):
    """function to find a word in a string using bi-section method
    input : suffix array, query string and string to find the query string in
    output : query string matching location as a list
    code credit : https://stackoverflow.com/questions/49500809/
    find-all-occurrences-using-binary-search-in-a-suffix-array"""
    if lo < 0:
        raise ValueError("must be non-negative")
    if hi is None:
        hi = len(array)
    while lo < hi:
        mid = (lo + hi) // 2
        if seq[array[mid] :] < query:
            lo = mid + 1
        else:
            hi = mid

    def match_at(i):
        return seq[i : i + len(query)] == query

    if not match_at(array[lo]):
        raise IndexError("there is not any index for the query")

    first = lo
    while first > 0 and match_at(array[first - 1]):
        first -= 1

    last = lo
    while match_at(array[last]):
        last += 1

    return array[first:last]


def main():
    parser = argparse.ArgumentParser(
        description="""find all occurrences of a query string in a genome"""
    )
    parser.add_argument(
        "-r", "--reference", required=True, help="input file in fasta format"
    )
    parser.add_argument(
        "-q", "--query", required=True, help="query string in fasta format"
    )

    args = parser.parse_args()
    ref_genome = args.reference
    query_genome = args.query

    genome = get_sequence(ref_genome)
    suffix_array = reverse_string(genome)
    query_seq = get_sequence(query_genome)
    print(find_word(suffix_array, query_seq, genome))


if __name__ == "__main__":
    sys.exit(main())
