#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson,urllib
if __name__ == '__main__':
    def _print(data):
        if isinstance(data, unicode): data = data.encode('utf-8')
        return data.strip()

    _list = {}
    for line in open('password.txt'):
        data = line.split('\t')
        _list[_print(data[0])] = _print(data[1])
    print _list
    simplejson.dump(_list, open('password.json','w'),indent=2,ensure_ascii=False)
