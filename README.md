## 说明

抓取猎聘网关于“数据 分析 上海”的相关职位，并做简单分析。

## 环境要求

本人使用 Anaconda2的环境， 使用pip安装了Scrapy 1.4.0

```
Python 2.7.14 :: Anaconda, Inc.
Scrapy 1.4.0
```

## 基本操作

抓取数据，直接运行：

```
python run.py
```
数据会保存在目录data下，当天日期命名的csv。

或者

```
scrapy crawl jb -o data.csv
```

## 更多信息

参见我的博客介绍：[Python爬虫之Scrapy上手指南](http://www.fr4nk.cn/2017/11/28/scrapy-tutorial/)