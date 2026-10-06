from parser import load_fasta

from dna_operations import DnaSequence

from orf_dir import orf_maker_inputs

from Filter import LengthFilter
from Filter import WeightFilter
from Filter import apply_filters
from Filter import load_amino_weights

from output import annotation
from output import logger
from output import reporter

from pathlib import Path
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--min-length", required=True, type=int)
    args = parser.parse_args()

    BASE_DIR = Path(__file__).resolve().parent
    OUTPUT_DIR = Path(args.out)
    OUTPUT_DIR.mkdir(exist_ok=True)

    LOG_FILE = OUTPUT_DIR / "bioforge.log"
    REPORT_FILE = OUTPUT_DIR / "report.txt"
    WEIGHTS_FILE = BASE_DIR / "data" / "amino_weights.txt"


    my_logger = logger(LOG_FILE)
    my_reporter = reporter(REPORT_FILE)


    my_logger.log("BioForge pipeline started")

    fasta_result = load_fasta(args.input)

    list_of_sequences = []
    for value in fasta_result.values():
        for key, value in value.items():
            if key == "sequence":
                list_of_sequences.append(value)

    rna_result = DnaSequence(list_of_sequences)
    rna_strands = rna_result.rna_strands()

    all_orfs = orf_maker_inputs(rna_strands)

    my_logger.log(f"Total ORFs found: {len(all_orfs)}")
    print(f"Total ORFs found: {len(all_orfs)}")
    print("=" * 40)

    amino_weights = load_amino_weights(WEIGHTS_FILE)
    my_logger.log(f"Amino weights loaded: {len(amino_weights)} entries")

    min_length = args.min_length
    min_weight = 0
    max_weight = 100000

    length_filter = LengthFilter(min_length=min_length)
    weight_filter = WeightFilter(
        amino_weights,
        min_weight=min_weight,
        max_weight=max_weight,
    )

    filtered_orfs = apply_filters(
        all_orfs,
        [length_filter, weight_filter]
    )

    my_logger.log(f"After filters: {len(filtered_orfs)}")
    print(f"After filters: {len(filtered_orfs)}")
    print("=" * 40)

    annotated_orfs = annotation(filtered_orfs)

    my_reporter.report("=" * 60)
    my_reporter.report("BioForge Report")
    my_reporter.report("=" * 60)

    for orf in annotated_orfs:
        my_reporter.report(f"ID:        {orf['ID']}")
        my_reporter.report(f"Strand:    {orf['strand']}")
        my_reporter.report(f"Frame:     {orf['frame']}")
        my_reporter.report(f"Start Pos: {orf['start_pos']}")
        my_reporter.report(f"Protein:   {orf['protein']}")
        my_reporter.report(f"Complete:  {orf['is_complete']}")
        my_reporter.report("-" * 60)

    my_reporter.report(f"Total ORFs: {len(annotated_orfs)}")

    my_logger.log(f"Report written to {REPORT_FILE}")
    my_logger.log("BioForge pipeline finished")

    print(f"\n Report saved to: {REPORT_FILE}")
    print(f" Log saved to: {LOG_FILE}")


if __name__ == "__main__":
    main()