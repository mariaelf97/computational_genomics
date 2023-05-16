#!/usr/bin/env python3
import sys

import pandas as pd


def main():
    df = pd.read_csv(
        "/ocean/projects/bio230002p/ahmadije/final_project/mpox-snps-header-removed.tsv",
        sep="\t",
        index_col=False,
    )
    variant_count = (
        df.groupby(["[P1]", "[SUB]", "[SUB].1"]).size().to_frame().reset_index()
    )
    variant_count = variant_count.rename(
        columns={"[P1]": "position", "[SUB]": "ref", "[SUB].1": "alt", 0: "samples"}
    )
    variant_count = variant_count.sort_values("samples", ascending=False)
    annotation = pd.read_csv(
        "/ocean/projects/bio230002p/ahmadije/final_project/vep_final.txt",
        sep="\t",
        index_col=False,
    )
    # change location to be able to merge with the main variant counts file
    annotation["Location"] = annotation["Location"].str.split(":").str[-1]
    annotation["Location"] = annotation["Location"].astype(str)
    variant_count["position"] = variant_count["position"].astype(str)
    joined_frames = pd.merge(
        annotation, variant_count, left_on="Location", right_on="position"
    )
    joined_frames = joined_frames.sort_values("samples", ascending=False)
    joined_frames["distance"] = joined_frames["Extra"].str.split(";", expand=True)[1]
    joined_frames["distance"] = joined_frames["distance"].str.split(
        "DISTANCE=", expand=True
    )[1]
    subset_df = joined_frames[
        [
            "ref",
            "alt",
            "Location",
            "Feature",
            "Consequence",
            "distance",
            "Amino_acids",
            "Protein_position",
            "samples",
        ]
    ]
    subset_df.to_csv("variant_counts_consequences.csv")


if __name__ == "__main__":
    sys.exit(main())
