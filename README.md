# Storage_Box.md
#### 简单的日志功能
```python
from logs import Log

class Test:
	def __init__(self, log=print):
		self.log = log

	def save_log(self, info):
		self.log(info)

log = Log('./log')
t = Test(log)
t.save_log('保存输出到日志中...')

```