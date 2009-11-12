#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

if __name__ == '__main__':
    def _print(data):
        if isinstance(data, unicode): data = data.encode('utf-8')
        print data
        return data.strip()
    _list = {}

    for line in open('src.txt'):
        datas = line.split('\t')
        devil_name = _print(datas[3])
        src_name = _print(datas[4])
        skills = datas[5].split('・')
        skill_list = []
        for skill in skills:
            skill_list.append({
                'name':_print(skill),
                'urlencode': urllib.quote_plus(_print(skill))
                })
        _list[devil_name] = {
            'src_name':src_name,
            'skills':skill_list
            }
        
        
    import simplejson
    from datetime import datetime
    print datetime.now(),_list
    simplejson.dump(_list, open('src.json','w'),indent=2,ensure_ascii=False)
