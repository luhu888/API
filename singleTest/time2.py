# __author__=luhu
# -*- coding: utf-8 -*-
import datetime
# 获取当前时间
d1 = datetime.datetime.now()
print(d1.strftime('%Y{y}%m{m}%d{d}%H{H}%M{M}%S{S}').format(y='年', m='月', d='日', H='时', M='分', S='秒'))

