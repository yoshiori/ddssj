#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import simplejson

skill_data = simplejson.load(open('all_skill.json'))
detail_data = simplejson.load(open('devil_detail_dic.json'))
demonica_modoki_data = simplejson.load(open('demonica_modoki.json'))


def _print(data):
    if isinstance(data, unicode): data = data.encode('utf-8')
#    print data
    return data.strip()

def get_has_devil(name):
    devils = []
    for devil_name,detail in detail_data.items():
        if devil_name == u'デモニカもどき':
            has = False
            for modoki in demonica_modoki_data:
                for skill in modoki['skill']:
                    if name == skill['name']:
                        has =True
            if has:
                devils.append(u'デモニカもどき')
            continue
        for skill in detail['skill']:
            if skill['name'] == name:
                devils.append(devil_name)
    return devils

def get_src_devil(name):
    devils = []
    for devil_name,detail in detail_data.items():
        if devil_name == u'デモニカもどき':
            has = False
            for modoki in demonica_modoki_data:
                for skill in modoki['src']['skills']:
                    if name == skill['name']:
                        has =True
            if has:
                devils.append(u'デモニカもどき')
            continue
        for skill in detail['src']['skills']:
            if skill['name'] == name:
                devils.append(devil_name)
    return devils


def _dump(data):
    file = open('skill_detail.json','w')
    file.write(
        simplejson.dumps(data,
                    indent=2,ensure_ascii=False)
            )
    file.close()

def _dump2(data):
    simplejson.dump(data, open('skill_detail.json','w'),indent=2,ensure_ascii=False)

    
if __name__ == '__main__':

    skill_detail = {}
    for skill_name,data in skill_data.items():
        skill = _print(skill_name)
        skill_detail[skill]={
            'name':skill,
            'type':_print(data['type']),
            'urlencode': urllib.quote_plus(skill),
            'detail':_print(data['detail']),
            'sort':data['sort']
            }
        devils = get_has_devil(skill_name)
        devil_data = []
        for devil in devils:
            devil_data.append({
                'name':_print(devil),
                'urlencode':urllib.quote_plus(_print(devil))
                })
        skill_detail[skill]['devils'] = devil_data
        devils = get_src_devil(skill_name)
        src_data = []
        for devil in devils:
            src_data.append({
                'name':_print(devil),
                'urlencode':urllib.quote_plus(_print(devil))
                })
        skill_detail[skill]['src'] = src_data
        if data.has_key('mp'):
            skill_detail[skill]['mp'] = data['mp']
    _dump(skill_detail)
    from datetime import datetime
    print 'finish',datetime.now()
