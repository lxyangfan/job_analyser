## 说明

抓取猎聘网关于“数据 分析 上海”的相关职位，并做简单分析。

## 环境要求

本人使用 Anaconda2的环境， 使用pip安装了Scrapy 1.4.0

```
Python 2.7.14 :: Anaconda, Inc.
Scrapy 1.4.0
```

## 基本操作

抓取数据

```
scrapy crawl jb -o items.csv
```