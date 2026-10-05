# نیازمند ورودی یک لیست به شکل مجموعه تاپلها (rna-string , strand-string : forward/reverse_complement(rc))
from translator import translate
from orf_class import ORF
from dna import  R_S_LIST

# solution_for_input = """
# my_list_of_tuples = [("rna1" , "strand1"),("rna2" , "strand2"),("rna3" , "strand3")]

# for i in my_list_of_tuples:
#     x = orf_maker(i[0] , i[1])
#     print(x)
# """

def orf_maker_inputs(rnas_strands): # برای بدست اوردن orf های نهایی ازین کد استفاده می کنیم
    all_orfs = []

    for i in rnas_strands:
        x = orf_maker_construction(i[0], i[1])
        all_orfs.extend(x)

    return all_orfs

def orf_maker_construction(rna, strand):

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
                    orf,
                    protein,   
                    strand,
                    frame,
                    start_pos,
                    is_complete,
                    )

            # orfs.append(orfs.append(orf_object)) # شی واقعی و نمایش با __reper__
            orfs.append(orf_object.orf_make_real()) # ساخت دیکشنری از اشیا نه واقعا این که خود شی باشه
            i = j + 3 # به بعد از اخرین استاپ کدون رفته و مابقی فریم را برای پیدا کردن orf جدید بررس می کنیم 

    return orfs 

# x = orf_maker("AUGAAugAcgcgcgcgcgCCCGGGUAGCCCUAA" , "forward")
# print(x)
# print(type(x))
# print(len(x))

last_output = orf_maker_inputs(R_S_LIST)
print(last_output)

for i in last_output:
    for key in i.keys(): #برای ورودی صادق
        if key == "codons" :
            print(i["codons"])
    # print(type(i))
    # break