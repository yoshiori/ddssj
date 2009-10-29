#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    list = []
    for line in open('skill.txt'):
        list.append([text.rstrip() for text in line.split('\t')])

    for data in list:
        for text in data:
            print text,
        print 
            
    import simplejson
    simplejson.dump(list, open('skill.json','w'),indent=2,ensure_ascii=False)
