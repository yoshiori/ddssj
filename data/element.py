#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson

if __name__ == '__main__':
    data = {}
    for line in open('element.txt'):
        text = line.split('\t')
        data[text[3]] = [x.strip() for x in text[4].split('、')]

    print data
    simplejson.dump(data, open('element.json','w'),indent=2,ensure_ascii=False)
