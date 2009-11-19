#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
def _print(data):
    if isinstance(data, unicode): data = data.encode('utf-8')
#    print data
    return data.strip()

count = 0

def create(path, _type=None):
    global count
    data = {}
    detail_index = 3
    if _type:
        detail_index = 2
    for skill in open(path):
        __type = _type
        detail =  skill.split('\t')
        if not __type:
            __type = _print(detail[2])
        data[_print(detail[0])] = {
            'mp':int(detail[1]),
            'type':__type,
            'detail':_print(detail[detail_index]),
            'sort': count
            }
        count += 1
    return data

def create_auto(path):
    global count
    data = {}
    detail_index = 1
    for skill in open(path):
        detail =  skill.split('\t')
        data[_print(detail[0])] = {
            'type':'自動',
            'detail':_print(detail[detail_index]),
            'sort':count
            }
        count += 1
    return data

if __name__ == '__main__':

    _list = {}
    _list.update(create('skill_attack.txt'))
    _list.update(create('skill_magic.txt'))
    _list.update(create('skill_heal.txt','回復'))
    _list.update(create('skill_hojyo.txt','補助'))
    _list.update(create_auto('skill_auto.txt'))
    import simplejson
    from datetime import datetime
    print datetime.now()
    simplejson.dump(_list, open('all_skill.json','w'),indent=2,ensure_ascii=False)
