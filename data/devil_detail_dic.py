#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson,urllib
if __name__ == '__main__':
    detail_data = simplejson.load(open('devil_detail.json'))
    def _print(data):
        if isinstance(data, unicode): data = data.encode('utf-8')
        return data
    _list = {}
    for name,data in detail_data.items():
#        print name.encode('utf_8')
        if name.encode('utf-8') == 'デモニカもどき':
            print 'fff'
            continue
        detail = {}
        detail['lv'] = _print(data[0])
        detail['type'] = _print(data[1])
        detail['name'] = _print(data[2])
        skills = []
        for i in range(3,6):
            if data[i]:
                skills.append(_print(data[i]))
        detail['skill'] = skills
        detail['attack'] = _print(data[6])
        detail['shot'] = _print(data[7])
        detail['fire'] = _print(data[8])
        detail['ice'] = _print(data[9])
        detail['electric'] = _print(data[10])
        detail['force'] = _print(data[11])
        detail['expel'] = _print(data[12])
        detail['death'] = _print(data[13])
        detail['attack_type'] = _print(data[14])
        detail['stance'] = _print(data[16])
        detail['hp'] = _print(data[17])
        detail['mp'] = _print(data[18])
        detail['strength'] = _print(data[19])
        detail['magic'] = _print(data[20])
        detail['vitality'] = _print(data[21])
        detail['speed'] = _print(data[22])
        detail['luck'] = _print(data[23])
        detail['urlencode'] = urllib.quote_plus(_print(name))
        detail['test'] ='test'
        _list[_print(name)] = detail
    file = open('devil_detail_dic.json','w')
    file.write(
        simplejson.dumps(_list,
                    indent=2,ensure_ascii=False)
            )
    file.close()
    from datetime import datetime
    print 'finish',datetime.now()

