# -*- coding: utf-8 -*-
__author__ = "YuDian"
class hello(object):
    pass

print(getattr(hello,'good',None))
# 还是要加上None。不然会返回错误。加上None会得到None。

# 但是:def getattr(object, name, default=None):   这里default不是有默认值么？？？
