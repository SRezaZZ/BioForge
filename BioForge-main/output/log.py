class logger:

    def __init__(self, logfile):
        self.logfile = logfile

    def log(self, message):
        with open(self.logfile, 'a', encoding='utf-8') as l:
            l.write(message + "\n")