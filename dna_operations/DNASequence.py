from datetime import datetime
class DnaSequence:
    def __init__(self, sequence):
        self.sequence = [seq.upper() for seq in list(sequence.values())]
        self.valid_bases = {"A", "T", "C", "G"}
        self.validation()

    def validation(self):
        try:
            for dna in self.sequence:
                if not set(dna).issubset(self.valid_bases):
                    raise Exception("InvalidSequenceError")
        except Exception as dna_operation_error:
            with open("bioforge.log", "a") as file:
                file.write(f"{datetime.now()} - {dna_operation_error}\n")

    def complement(self):
        complemented = self.sequence.copy()

        for i in range(len(complemented)):
            dna = list(complemented[i])

            for j in range(len(dna)):
                if dna[j] == 'A':
                    dna[j] = 'T'
                elif dna[j] == 'T':
                    dna[j] = 'A'
                elif dna[j] == 'C':
                    dna[j] = 'G'
                elif dna[j] == 'G':
                    dna[j] = 'C'

            complemented[i] = "".join(dna)

        return complemented

    def reverse_complement(self):
        rev_complemented = self.complement()

        for i in range(len(rev_complemented)):
            rev_complemented[i] = rev_complemented[i][::-1]

        return rev_complemented
    
    def dna_to_rna(self):
        d_to_r = self.sequence.copy()

        for i in range(len(d_to_r)):
            d_to_r[i] = d_to_r[i].replace("T", "U")

        return d_to_r

    def gc_content(self):
        total_gc_percent = 0

        for seq in self.sequence:
            c_count = seq.count("C")
            g_count = seq.count("G")
            total_gc_percent += ((c_count + g_count) / len(seq)) * 100

        return total_gc_percent / len(self.sequence)

    def rna_strands(self):
        rna_strands = []

        for rna in self.dna_to_rna():
            rna_strands.append((rna, "forward"))

        for dna in self.reverse_complement():
            rna = dna.replace("T", "U")
            rna_strands.append((rna, "reverse_complement"))

        return rna_strands