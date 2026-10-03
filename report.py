class reporter :

    def __init__(self, reportfile):
        self.reportfile = reportfile

    def report(self, data) : # ایجاد فایل report.tx
        with open (self.reportfile, 'a') as r :
                r.write(data)