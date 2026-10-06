from parser import load_fasta
from dna_operations import DNASequence
from ORF import orf_class
from ORF import orf_maker
from ORF import translator
from Filter import filters
from output import annotation
import argparse
import os
from output import log
from output import report
from exceptions import BioForgeError


def main() : # CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--out")
    parser.add_argument("--min_length", type=int)
    args = parser.parse_args()
    logfile = os.path.join(args.out, "bioforg.log") # چسباندن مسیر فایل خروجی لاگ
    reportfile = os.path.join(args.out, "report.txt") # چسباندن مسیر فایل خروجی ریپورت
    log(logfile) # دادن مسیر فایل لاگ به ماژول
    report(reportfile) # دادن مسیر فایل ریپورت به ماژول
    load_fasta(args.input) # فایل input جهت ارجاع به تابرع یا فایل فستاپارسنگ
    filters(args.min_length) # جهت ارجاع min-lenght به تابع یا فایل فیلترینگedit


if __name__ == "__main__":
    main()
