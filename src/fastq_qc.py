#
import sys

import pandas as pd
import seaborn as sns
from Bio import SeqIO


def calculate_score():
    """function to get quality score for each base in all reads"""
    qual_list = []
    base_list = []
    for record in SeqIO.parse("/Users/maryam/Downloads/assignment1.fastq", "fastq"):
        qual_score = record.letter_annotations["phred_quality"]
        qual_base = record.seq
        qual_list.append(qual_score)
        base_list.append(qual_base)
    return qual_list, base_list


def create_graphs(df, density=True):
    if density:
        sns.kdeplot(df, x="quality_score", hue="base").set(
            title="Quality distribution per base"
        )
    else:
        sns.set(font_scale=0.6)
        sns.boxplot(x="position_in_read", y="quality_score")


def main():

    df_list = []
    qual_scores, qual_bases = calculate_score()[0], calculate_score()[1]
    for i in range(0, len(qual_scores)):
        for j in range(1, len(qual_scores[1])):
            df_list.append(
                {
                    "read_number": i,
                    "position_in_read": j,
                    "base": qual_bases[i][j],
                    "quality_score": qual_scores[i][j],
                }
            )
    qual_df = pd.DataFrame(df_list)
    # get summary stats
    print(qual_df["quality_score"].describe())
    # get density plot per base
    create_graphs(qual_df, density=True)
    # get box plot of quality scores
    create_graphs(qual_df, density=False)


if __name__ == "__main__":
    sys.exit(main())
