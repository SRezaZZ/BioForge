class ORF:

    count = 1

    def id_maker(self):
        x = ORF.count
        ORF.count += 1

        if x < 10:
            return f"BFG_00{x}"
        elif x < 100:
            return f"BFG_0{x}"
        else:
            return f"BFG_{x}" # متغیر کلاسی برای ساخت ID
    def __init__(self,codons ,protein ,strand ,frame ,start_pos ,is_complete ):
        self.id = self.id_maker()
        self.codons = codons
        self.protein = protein
        self.strand = strand
        self.frame = frame
        self.start_pos = start_pos
        self.is_complete = is_complete

    # def __repr__(self):
    #     return (
    #         f"ORF("
    #         f"ID = {self.id} , "
    #         f"codons = {self.codons} , "
    #         f"protein = {self.protein} , "
    #         f"strand = {self.strand} , "
    #         f"frame = {self.frame} , "
    #         f"start_pos = {self.start_pos} , "
    #         f"is_complete = {self.is_complete}  "
    #         f")"
    #     )
    
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
