from translator import translate
from orf_class import ORF
def orf_maker(rna, strand):

    rna = rna.upper()
    rna_length = len(rna)
    stop_codons = ["UAA", "UAG", "UGA"]
    orfs = []

    for frame in range(3):

        i = frame

        while i <= rna_length - 3: # تا آخرین کدون سه تایی کامل چک میکنیم

            codon = rna[i:i + 3] # سه تا سه تا چک میکنیم

            if codon != "AUG": # اگر پیدا نکردیم دوباره برمیگردیم برای سه تایی عدی
                i += 3
                continue

            start_index = i # نقزه شروع
            orf = [codon]
            is_complete = False

            j = i + 3 # کدون بعدی میشود سه تا بعدی
            while j <= rna_length - 3:

                codon = rna[j:j + 3] # سه تا سه تابرای هر کدون جلو میرویم

                if codon in stop_codons: # آیا به استاپ رسیدیم
                    is_complete = True
                    break

                orf.append(codon) # به orf اضافه می کنیم
                j += 3

            if strand == "forward": # تعیین نقطه شروع
                start_pos = start_index

            else: #تعیین نقطه شروع در صورت معکوس بودن 
                start_pos = rna_length - start_index - 1 

            protein = translate(orf)
            orf_object = ORF(
                    strand,
                    frame,
                    start_pos,
                    orf,
                    is_complete,
                    protein
                    )

            orfs.append(orf_object.orf_make_real())

            i = j + 3 # به بعد از اخرین استاپ کدون رفته و مابقی فریم را برای پیدا کردن orf جدید بررس می کنیم 

    return orfs 

# x = orf_maker("AUGAAAUAcgcgcgcgcgCCCGGGUAGCCCUAA" , "forward")
# print(x)
# print(type(x))
# print(len(x))