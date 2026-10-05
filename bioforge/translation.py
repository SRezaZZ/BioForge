from .exceptions import DataFileError
from .models import ProteinSequence


def translate_orf(orf, codon_table):

    amino_acids = []

    for position in range(
        0,
        len(orf.rna_sequence) - 2,
        3,
    ):
        codon = orf.rna_sequence[
            position:position + 3
        ]

        if codon not in codon_table:
            raise DataFileError(
                f"Codon '{codon}' is missing "
                "from the codon table."
            )

        amino_acid = codon_table[codon]

        if amino_acid == "*":
            break

        amino_acids.append(amino_acid)

    protein_sequence = "".join(amino_acids)

    orf.protein = ProteinSequence(
        protein_sequence
    )

    return orf


def translate_orfs(orfs, codon_table):

    for orf in orfs:
        translate_orf(
            orf,
            codon_table,
        )

    return orfs