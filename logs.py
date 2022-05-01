import os
from dates import Date

class Log:
    def __init__(self, log_dir) -> None:
        self.log_dir = log_dir
        self.date = Date.get_today()
        self._check_dir()

    def _check_dir(self):
        '''检查日志的路径'''
        self.path = '{0}/{1}.log'.format(self.log_dir, self.date)
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            self._mkdir_dir()
    
    def _mkdir_dir(self):
        '''创建日志文件'''
        open(self.path, 'w', encoding='utf-8').close()

    def log(self, info):
        '''写入日志'''
        date = Date.get_today()
        if date != self.date:
            self.date = date
            self._check_dir()
        with open(self.path, 'a', encoding='utf-8') as f:
            f.write('{0} {1} {2}\n'.format(date, Date.now_date(), info))

    def __call__(self, info):
        self.log(info)
