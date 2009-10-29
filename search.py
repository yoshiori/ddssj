#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import simplejson
from django.utils import simplejson
import os

gousei_data = simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/gousei.json')))
detail_data = simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/devil_detail_dic.json')))
tokusyu_data = simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/tokusyu.json')))
element_data = simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/element.json')))

devil_list ={}

for data in detail_data.values():
    key = data['type']
    if devil_list.has_key(key):
        devil_list[key].append(data)
    else:
        devil_list[key] = [data]

def search_result(data,minmax):
    list1 = devil_list[data[0]]
    list2 = devil_list[data[1]]
    _list = []
    for devil1 in list1:
        for devil2 in list2:
            lv = (devil1['lv'] + devil2['lv']) / 2
            if minmax[0] < lv <= minmax[1]:
                _list.append((devil1,devil2))
    return _list

def get_min_max(devil):
    level = devil['lv'];
    _max = 100;
    _min = 0
    devils = devil_list[devil['type']]
    for dev in devils:
        if tokusyu_data.has_key(dev['name']):
            continue
        _level = dev['lv']
        if level > _level and _min < _level:
            _min = _level + 1
        if level < _level and _max > _level:
            _max = _level
    if not _max == 100:
        _max = level
    return _min,_max

def search_normal(devil):
    gousei = gousei_data[devil['type']]
    min_max = get_min_max(devil)
    results = []
    for result in gousei:
        result = tuple(result)
        details = search_result(result,min_max)
        if details:
            results.append({'type':result,
                           'details':details,
                           })
    return results

def search_element(devil):
    name = devil['name']
    if element_data.has_key(name):
        results = []
        for result in element_data[name]:
            result = (result,result)
            results.append({'type':result})
        return results
    
def search_special(devil):
    name = devil['name']
    if tokusyu_data.has_key(name):
        data = tokusyu_data[name]
        _list = []
        for dev in data:
            _list.append(detail_data[dev])
        return _list
    
if __name__ == '__main__':
 
    import sys
    text = u'リリム'
    text = u'エアロス'

    if 1 < len(sys.argv):
        text = unicode(sys.argv[1],'utf-8')
        print text
    devil = detail_data.get(text)
    if not devil:
        print '404'
    special_result = search_special(devil)
    if special_result:
        for result in special_result:
            print result['name'].encode('utf-8'),
    else:
        for data in (search_element(devil) or search_normal(devil)):
            print data['type'][0].encode('utf-8'),data['type'][1].encode('utf-8')
            if data.has_key('details'):
                for _data in data.get('details'):
                    for foo in _data:
                        print foo['name'].encode('utf-8'),foo['urlencode']
                    print
                print

