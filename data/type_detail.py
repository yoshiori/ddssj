#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
def _print(data):
    if isinstance(data, unicode): data = data.encode('utf-8')
#    print data
    return data.strip()

if __name__ == '__main__':
    type_data = {}
    count = 0
    for line in open('type_detail.txt'):
        if not line.startswith('#'):
            type_data[_print(line)] = count
            count += 1

    import simplejson
    from datetime import datetime
    print datetime.now()
    simplejson.dump(type_data, open('type_detail.json','w'),indent=2,ensure_ascii=False)

