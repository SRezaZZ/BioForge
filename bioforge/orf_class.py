from annotation import annotation

class ORF:

    # کلاسی برای ساخت ID
    def __init__(self,codons ,protein ,strand ,frame ,start_pos ,is_complete ):
        self.id = anotation(orf)
        # ORF.annotation += 1
        self.codons = codons
        self.protein = protein
        self.strand = strand
        self.frame = frame
        self.start_pos = start_pos
        self.is_complete = is_complete


    def orf_make_real(self): 
        return {
            "ID":self.id,
            "codons": self.codons,
            "protein": self.protein,
            "strand": self.strand,
            "frame": self.frame,
            "start_pos": self.start_pos,
            "is_complete": self.is_complete,
        }
