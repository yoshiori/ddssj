#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson

if __name__ == '__main__':
    data = {}
    key = None
    for line in open('mitama.txt'):
        text = line.split('\t')
        if len(text) == 2:
            key = text[0].strip()
            names = text[1].split('×')
            data[key] = [(names[0].strip(),names[1].strip())]
        else:
            names = line.split('×')
            data[key].append((names[0].strip(),names[1].strip()))
    print data
    simplejson.dump(data, open('mitama.json','w'),indent=2,ensure_ascii=False)
