class ORF:

    annotation = 0 # متغیر کلاسی برای ساخت ID
    def __init__(self,codons ,protein ,strand ,frame ,start_pos ,is_complete ):
        self.id = ORF.annotation
        ORF.annotation += 1
        self.codons = codons
        self.protein = protein
        self.strand = strand
        self.frame = frame
        self.start_pos = start_pos
        self.is_complete = is_complete


    def orf_make_real(self): 
        return {
            "ID":self.annotation,
            "codons": self.codons,
            "protein": self.protein,
            "strand": self.strand,
            "frame": self.frame,
            "start_pos": self.start_pos,
            "is_complete": self.is_complete,
        }
