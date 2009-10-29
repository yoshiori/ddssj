#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    count = 0
    data = []
    for line in open('text'):
        if count > 0:
            count -= 1
            continue
        if line == '\n':
            count = 3
            continue
        data.append(line.rstrip())
    data2 = {}
    for line in data:
        adata = [text.rstrip() for text in line.split('\t')]
        data2[adata[3]] = adata
        print line ,
    
    import simplejson
    simplejson.dump(data2, open('status.json','w'),indent=2,ensure_ascii=False)
