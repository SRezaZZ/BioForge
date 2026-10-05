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