#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson

if __name__ == '__main__':
    data = {}
    elements = ['',
                'サラマンダー',
                'ウンディーネ',
                'シルフ',
                'ノーム',
                'フレイミーズ',
                'アクアンズ',
                'エアロス',
                'アーシーズ'
                ]
    a = {'↓': -1,
         '↑1': 1,
         '↑2': 2,
         }
    for line in open('element-up.txt'):
        text = [x.strip() for x in line.split('\t')]
        results = {}
        for i in range(1, len(elements)):
            results[elements[i]] = a[text[i]]
        data[text[0]] = results
        

    simplejson.dump(data, open('element-up.json','w'),indent=2,ensure_ascii=False)
