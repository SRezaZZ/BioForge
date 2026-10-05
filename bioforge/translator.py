from os import getcwd , path

def load_codon_table():

    base = path.dirname(path.abspath(__file__)) # برای گرفتن بیس مسیر فایلی که در حال حاضر دارم داخلش کد میزنم
    codon_Table = path.join(base , "data", "codon_table.txt") # جمع میکنم با مسیر نسبی

    table = {}
    line_number = 0

    try:
        with open(codon_Table, encoding="utf-8") as f:
            for line in f:
                line_number += 1
                line = line.strip()          # حذف فاصله های طرفین در صورتی که وجود داشته باشم

                if line == "" or line.startswith("#"): # خط خالی و کامنت در نظر نمیگیریم
                    continue

                codon_amino = line.split()         # به لیست تبدیلش میکنیم
                if len(codon_amino) != 2:
                    raise SyntaxError(f"Line-{line_number}- : {line} ---> is not correct")

                codon = codon_amino[0].upper() # کدون قسمت اول
                amino = codon_amino[1].upper() # آمینو اسید قسمت دوم

                if len(codon) != 3: # بررسی تعداد حروف کدون
                    raise SyntaxError(f"line-{line_number}- : {codon} Codon must be 3 words")
                if len(amino) != 1: # بررسی تعداد حروف آمینو اسید
                    raise SyntaxError(f"Line-{line_number}- : {amino} Amino acid must be 1 word")

                table[codon] = amino # ساخت دیکشنری

    except FileNotFoundError:
        raise ValueError(f"File not found : {path}") #زمانی که فایل وجود نداشته باشد

    if len(table) == 0:
        raise ValueError(f"File is empty : {path}") #زمانی که فایل وجود خالی باشد

    return table

# codons = ["UUU", "UUC", "UUA", "UUG", "UAA", "UGA" , "GGG"]
codon_table = load_codon_table()
def translate(codons):

    protein = ""
    for codon in codons:
        if codon not in codon_table:
            raise ValueError(f"Unknown Codon : {codon}")
        amino = codon_table[codon]
        if amino == "*": 
            break
        protein += amino
    return protein

# x = translate(codons)
# print(x)