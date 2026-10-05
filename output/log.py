class logger :

    def __init__(self, logfile):
        self.logfile = logfile

    def log(self, message) : # ایجاد قایل جهت ذخیره سازی log ها
        with open (self.logfile, 'a') as l :
            l.write(message)