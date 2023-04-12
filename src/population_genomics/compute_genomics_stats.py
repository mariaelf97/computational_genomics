#!/usr/bin/env python3
import argparse
import sys

import pandas as pd


def main():
    parser = argparse.ArgumentParser(
        description=""" program to get get heterozygosity and allele frequency using vcftools out.het and out.freq"""
    )
    parser.add_argument(
        "-i1", "--input1", required=True, help="vcftools out.het output"
    )
    parser.add_argument(
        "-i2", "--input2", required=True, help="vcftools out.frq output"
    )

    args = parser.parse_args()
    out_het = args.input1
    out_freq = args.input2
    vcf_input = pd.read_csv(out_het, sep="\t")
    vcf_input["heterozygosity"] = (
        vcf_input["N_SITES"] - vcf_input["O(HOM)"]
    ) / vcf_input["N_SITES"]
    heterozygosity_per_ind = vcf_input[["INDV", "heterozygosity"]]
    heterozygosity_per_ind.to_csv("heterozygosity.tsv", sep="\t")
    allele_freq_input = pd.read_csv(out_freq, sep="\t")
    allele_freq_output = allele_freq_input[["CHROM", "{FREQ}"]]
    allele_freq_output["allele_2_freq"] = 1 - allele_freq_output["{FREQ}"]
    allele_freq_output.rename(
        columns={
            "CHROM": "locus",
            "{FREQ}": "allele_1_freq",
            "allele_2_freq": "allele_2_freq",
        },
        inplace=True,
    )
    allele_freq_output.to_csv("allele_frequency.tsv", sep="\t")


if __name__ == "__main__":
    sys.exit(main())
