#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson
except:
    from django.utils import simplejson
import os

gousei_data = simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/gousei.json')))
detail_data = simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/devil_detail_dic.json')))
special_data = simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/tokusyu.json')))
element_data = simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/element.json')))
element_up_data = simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/element-up.json')))
mitama_data =  simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/mitama.json')))

converter_type = {
    u'珍獣':u'魔獣',
    u'魔人':u'幻魔',
    u'魔神':u'秘神',
    }
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
            if minmax[0] <= lv <= minmax[1]:
                _list.append((devil1,devil2))
    return _list

def get_min_max(devil):
    level = devil['lv'];
    _max = 100;
    _min = 1
    devils = devil_list[devil['type']]
    for dev in devils:
        if special_data.has_key(dev['name']):
            continue
        _level = dev['lv']
        if level > _level and _min < _level:
            _min = _level + 1
        if level < _level and _max > _level:
            _max = _level - 1
    if not _max == 100:
        _max = level
    return _min,_max

def search_normal(devil):
    return _search(devil['type'],get_min_max(devil))

def search_converter(devil):
    _type = converter_type.get(devil['type'])
    if not _type:
        return
    return _search(_type,get_min_max(devil))

def search_kyoshin(devil):
    return u'狂神' == devil['type']

def _search(type,min_max):
    gousei = gousei_data.get(type)
    results = []
    if not gousei:
        return results
    for result in gousei:
        result = tuple(result)
        details = search_result(result,min_max)
        # 特殊合体に使うものは省く
        for detail in details:
            names =[detail[0]['name'],detail[1]['name']]
            for special in special_data.values():
                if set(names) == set(special):
                    details.remove(detail)
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

def search_element_up(devil):
    name = devil['type']
    if element_up_data.has_key(name):
        results = []
        lv = devil['lv']
        _list = sorted(devil_list[name],key=lambda x: x['lv'])
        index = _list.index(devil)
        for n,x in element_up_data[name].items():
            if 0 <= index + x < len(_list):
                results.append((
                    detail_data[n],
                    _list[index + x]
                    ))
        return results

def search_mitama(devil):
    name = devil['name']
    _list = []
    if mitama_data.has_key(name):
        for names in mitama_data[name]:
            _list.append((
                detail_data[names[0]],
                detail_data[names[1]]
                ))
        return [{'details':_list}]
            
def search_special(devil):
    name = devil['name']
    if special_data.has_key(name):
        data = special_data[name]
        _list = []
        for dev in data:
            _list.append(detail_data[dev])
        return _list

def _main2():
    text = u'リリム'
    devil = detail_data.get(text)
    results = search_element_up(devil)
    for detail in results:
        print detail[0]['name'].encode('utf-8'),detail[1]['name'].encode('utf-8')
    
def _main():
    import sys
    text = u'リリム'
    text = u'シヴァ'
    text = u'スフィンクス'
    #   text = u'エアロス'

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

def _main3():
    text = u'デイビット'
    devil = detail_data.get(text)
    for data in search_converter(devil):
        print data['type'][0].encode('utf-8'),data['type'][1].encode('utf-8')
        if data.has_key('details'):
            for _data in data.get('details'):
                for foo in _data:
                    print foo['name'].encode('utf-8'),foo['urlencode']
                print
            print
            
def _main4():
    text = u'クシミタマ'
    devil = detail_data.get(text)
    for data in search_mitama(devil):
        if data.has_key('details'):
            for _data in data.get('details'):
                for foo in _data:
                    print foo['name'].encode('utf-8'),foo['urlencode']
                print
            print

if __name__ == '__main__':
    _main()    
    #    _main2()
    #    _main3()
    #    _main4()
