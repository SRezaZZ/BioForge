from os import path
from exceptions import DataFileError


class BaseFilter:
    def apply(self, orfs):
        raise NotImplementedError


class LengthFilter(BaseFilter):

    def __init__(self, min_length):
        self.min_length = min_length

    def apply(self, orfs):
        filtered_orfs = []

        for orf in orfs:
            protein = orf["protein"]

            if len(protein) >= self.min_length:
                filtered_orfs.append(orf)

        return filtered_orfs


def load_amino_weights():

    data_dir = path.dirname(path.abspath(__file__))
    base_dir = path.dirname(data_dir)

    weights_file = path.join(
        base_dir,
        "data",
        "amino_weights.txt"
    )

    weights = {}
    line_number = 0

    try:
        with open(weights_file, encoding="utf-8") as file:

            for line in file:
                line_number += 1
                line = line.strip()

                if line == "" or line.startswith("#"):
                    continue

                parts = line.split()

                if len(parts) != 2:
                    raise DataFileError(
                        f"Invalid line {line_number}: {line}"
                    )

                amino = parts[0].upper()

                try:
                    weight = float(parts[1])
                except ValueError:
                    raise DataFileError(
                        f"Invalid weight at line {line_number}"
                    )

                weights[amino] = weight

    except FileNotFoundError:
        raise DataFileError(
            f"File not found: {weights_file}"
        )

    if len(weights) == 0:
        raise DataFileError(
            f"File is empty: {weights_file}"
        )

    return weights


class WeightFilter(BaseFilter):

    def __init__(self, min_weight=None, max_weight=None):
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.weights = load_amino_weights()

    def protein_weight(self, protein):

        total_weight = 18.015

        for amino in protein:

            if amino not in self.weights:
                raise ValueError(
                    f"Unknown amino acid: {amino}"
                )

            total_weight += self.weights[amino]

        return total_weight

    def apply(self, orfs):
        filtered_orfs = []

        for orf in orfs:

            protein = orf["protein"]
            weight = self.protein_weight(protein)

            if self.min_weight is not None:
                if weight < self.min_weight:
                    continue

            if self.max_weight is not None:
                if weight > self.max_weight:
                    continue

            filtered_orfs.append(orf)

        return filtered_orfs


class MotifFilter(BaseFilter):

    def __init__(self, motif):
        self.motif = motif.upper()

    def apply(self, orfs):
        filtered_orfs = []

        for orf in orfs:

            motifs = orf.get("motifs", [])

            for motif_info in motifs:

                if motif_info["motif"].upper() == self.motif:
                    filtered_orfs.append(orf)
                    break

        return filtered_orfs


def apply_filters(orfs, filters):

    result = orfs

    for filter_object in filters:
        result = filter_object.apply(result)

    return result



"""
from abc import ABC, abstractmethod


class Filter(ABC):

    @abstractmethod
    def matches(self, orf):

        pass


class LengthFilter(Filter):

    def __init__(self, min_length):
        if min_length < 0:
            raise ValueError(
                "min_length cannot be negative."
            )

        self.min_length = min_length

    def matches(self, orf):
        if orf.protein is None:
            raise ValueError(
                "ORF must be translated before filtering."
            )

        return len(orf.protein) >= self.min_length


class WeightFilter(Filter):

    def __init__(
        self,
        amino_weights,
        min_weight=None,
        max_weight=None,
    ):
        if (
            min_weight is not None
            and min_weight < 0
        ):
            raise ValueError(
                "min_weight cannot be negative."
            )

        if (
            max_weight is not None
            and max_weight < 0
        ):
            raise ValueError(
                "max_weight cannot be negative."
            )

        if (
            min_weight is not None
            and max_weight is not None
            and min_weight > max_weight
        ):
            raise ValueError(
                "min_weight cannot be greater "
                "than max_weight."
            )

        self.amino_weights = amino_weights
        self.min_weight = min_weight
        self.max_weight = max_weight

    def matches(self, orf):
        if orf.protein is None:
            raise ValueError(
                "ORF must be translated before filtering."
            )

        weight = orf.protein.molecular_weight(
            self.amino_weights
        )

        if (
            self.min_weight is not None
            and weight < self.min_weight
        ):
            return False

        if (
            self.max_weight is not None
            and weight > self.max_weight
        ):
            return False

        return True


class MotifFilter(Filter):

    def __init__(self, motif):
        motif = motif.strip().upper()

        if not motif:
            raise ValueError(
                "motif cannot be empty."
            )

        self.motif = motif

    def matches(self, orf):
        if orf.protein is None:
            raise ValueError(
                "ORF must be translated before filtering."
            )

        for match in orf.protein.motifs:

            if match["motif"] == self.motif:
                return True

        return False


def apply_filters(orfs, filters):

    filtered_orfs = orfs

    for current_filter in filters:

        filtered_orfs = [
            orf
            for orf in filtered_orfs
            if current_filter.matches(orf)
        ]

    return filtered_orfs
"""
