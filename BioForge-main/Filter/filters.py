from abc import ABC, abstractmethod


def load_amino_weights(weights_path):
    weights = {}
    with open(weights_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            amino_code = parts[0].upper()
            weight = float(parts[1])
            weights[amino_code] = weight
    return weights


class Filter(ABC):

    @abstractmethod
    def matches(self, orf):
        pass


class LengthFilter(Filter):

    def __init__(self, min_length):
        if min_length < 0:
            raise ValueError("min_length cannot be negative.")
        self.min_length = min_length

    def matches(self, orf):
        protein = orf["protein"]
        return len(protein) >= self.min_length


class WeightFilter(Filter):

    def __init__(self, amino_weights, min_weight=None, max_weight=None):
        if min_weight is not None and min_weight < 0:
            raise ValueError("min_weight cannot be negative.")

        if max_weight is not None and max_weight < 0:
            raise ValueError("max_weight cannot be negative.")

        if (min_weight is not None and max_weight is not None 
                and min_weight > max_weight):
            raise ValueError("min_weight cannot be greater than max_weight.")

        self.amino_weights = amino_weights
        self.min_weight = min_weight
        self.max_weight = max_weight

    def matches(self, orf):
        protein = orf["protein"]

        weight = 18.015
        for amino in protein:
            weight += self.amino_weights.get(amino, 0)

        if self.min_weight is not None and weight < self.min_weight:
            return False

        if self.max_weight is not None and weight > self.max_weight:
            return False

        return True


def apply_filters(orfs, filters):
    filtered_orfs = orfs
    for current_filter in filters:
        filtered_orfs = [
            orf for orf in filtered_orfs
            if current_filter.matches(orf)
        ]
    return filtered_orfs