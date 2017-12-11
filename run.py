# encoding=utf-8
import subprocess as sub
import os
from datetime import date

today = date.today()
ss = today.strftime("%Y%m%d")
print ss
filename = 'data/%s.csv' % ss
if os.path.isfile(filename):
    os.remove(filename)
    
handle = sub.Popen(['scrapy', 'crawl', 'jb', '-o', filename], stdout=sub.PIPE, stderr=sub.PIPE)


