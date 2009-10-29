#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    data = {}
    import re
    for line in open('tokusyu.txt'):
        foo = line.rstrip().split('\t')
        adata = foo[4]
        sozai = []
        for text in adata.split('×'):
            text = re.findall(u'[あ-ー]+',unicode(text,'utf-8'))[0]
            sozai.append(text)
        data[unicode(foo[3],'utf-8')] = sozai
    import simplejson
    file = open('tokusyu.json','w')
    file.write(
        simplejson.dumps(data,
            indent=2,ensure_ascii=False).encode('utf-8')
        )
    file.close()
