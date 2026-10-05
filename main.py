import argparse
import os
from filtering import filter
from log import log
from report import report
from fasta import fastaparsing

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
    fastaparsing(args.input) # فایل input جهت ارجاع به تابرع یا فایل فستاپارسنگ
    filter(args.min_length) # جهت ارجاع min-lenght به تابع یا فایل فیلترینگedit
