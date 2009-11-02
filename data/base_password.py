#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sufixs = ['low','neutral','chaos','etc']
    import re
    def removeTag(data):
        return re.sub('<.*?>','',data.strip())
    _list ={}
    for sufix in sufixs:
        for line in open('password-'+sufix+'.txt'):
            if line.startswith('<div class="ie5">'):
                _line = line.split('</tr>')
                for __line in _line:
                    if not __line.startswith('<div class="ie5">'):
                        text = __line.split('<td class="style_td">')
                        if len(text) == 16:
                            _list[removeTag(text[4])] = {'cost':removeTag(text[14]),
                                                     'password':removeTag(text[15]),
                                                     }
    import simplejson
    simplejson.dump(_list, open('base_password.json','w'),indent=2,ensure_ascii=False)

