import time

class Date:

    @classmethod
    def get_today(cls):
        return time.strftime(r'%Y-%m-%d', time.localtime())

    @classmethod
    def now_date(cls):
        return time.strftime('%H:%M:%S', time.localtime())
