class ORF:

    def __init__(self, strand, frame, start_pos, codons, is_complete, protein):
        self.strand = strand
        self.frame = frame
        self.start_pos = start_pos
        self.codons = codons
        self.is_complete = is_complete
        self.protein = protein

    def orf_make_real(self):
        return {
            "strand": self.strand,
            "frame": self.frame,
            "start_pos": self.start_pos,
            "codons": self.codons,
            "is_complete": self.is_complete,
            "protein": self.protein
        }