#!/usr/bin/env python3
import argparse
import io
import sys

import pandas as pd


def read_vcf(path):
    """code credit to :
    https://gist.github.com/dceoy/99d976a2c01e7f0ba1c813778f9db744"""
    with open(path, "r") as f:
        lines = [values for values in f if not values.startswith("##")]
    return pd.read_csv(
        io.StringIO("".join(lines)),
        dtype={
            "#CHROM": str,
            "POS": int,
            "ID": str,
            "REF": str,
            "ALT": str,
            "QUAL": str,
            "FILTER": str,
            "INFO": str,
            "FORMAT" : str,
        },
        sep="\t",
    ).rename(columns={"#CHROM": "CHROM"})


def main():

    input = read_vcf("/Users/maryam/Downloads/chr16.vcf")


if __name__ == "__main__":
    sys.exit(main())
