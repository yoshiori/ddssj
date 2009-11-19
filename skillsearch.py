#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson
except:
    from django.utils import simplejson
import os

skill_data = simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/skill_detail.json')))

skill_list ={}

for data in skill_data.values():
    key = data['type']
    if skill_list.has_key(key):
        skill_list[key].append(data)
    else:
        skill_list[key] = [data]
for datas in skill_list.values():
    datas.sort(key=lambda x: x.get('sort'))


def search(name):
    return skill_data.get(name)

if __name__ == '__main__':
    for key,data in skill_list.items():
        print key.encode('utf-8'),data
