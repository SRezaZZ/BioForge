class reporter:

    def __init__(self, reportfile):
        self.reportfile = reportfile

    def report(self, data):
        with open(self.reportfile, 'a', encoding='utf-8') as r:
            r.write(data + "\n")