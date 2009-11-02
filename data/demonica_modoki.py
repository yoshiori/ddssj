#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson
import urllib

if __name__ == '__main__':
    def _print(data):
        if isinstance(data, unicode): data = data.encode('utf-8')
        #print data
        return data.strip()
    _list = []
    for line in open('demonica_modoki.txt'):
        data = line.split('\t')
        name = data[3]
        detail = {}
        detail['lv'] = _print(data[0])
        detail['type'] = _print(data[2])
        detail['name'] = _print(data[3])
        skills = []
        for i in range(14,17):
            if data[i]:
                skills.append(_print(data[i]))
        detail['skill'] = skills
        detail['attack'] = _print(data[17])
        detail['shot'] = _print(data[18])
        detail['fire'] = _print(data[19])
        detail['ice'] = _print(data[20])
        detail['electric'] = _print(data[21])
        detail['force'] = _print(data[22])
        detail['expel'] = _print(data[23])
        detail['death'] = _print(data[24])
        detail['attack_type'] = _print(data[25])
        detail['stance'] = _print(data[1])
        detail['hp'] = _print(data[4])
        detail['mp'] = _print(data[5])
        detail['strength'] = _print(data[6])
        detail['magic'] = _print(data[7])
        detail['vitality'] = _print(data[8])
        detail['speed'] = _print(data[9])
        detail['luck'] = _print(data[10])
        detail['urlencode'] = urllib.quote_plus(_print(name))
        detail['password'] = _print(data[26])
        _list.append(detail)

        
    from datetime import datetime
    print datetime.now(),_list
    simplejson.dump(_list, open('demonica_modoki.json','w'),indent=2,ensure_ascii=False)
