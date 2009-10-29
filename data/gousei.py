#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    names = {'大天':'大天使',
             '破壊':'破壊神',
             '地母':'地母神',
             '堕天':'堕天使'}

    devils = []
    for name in open('devils.txt'):
        devils.append(name)

    gattai = []
    for text in open('gousei.txt'):
        gattai.append(text)

    data ={}    
    def getGattai(list,index):
        gousei = list[index].split('\t')
        for i,text in enumerate(gousei):
            if text == '−' or i <= index or i > len(devils):
                continue
            adata = [getName(devils[i-1].rstrip()),
                     getName(devils[index].rstrip())]
            text = getName(text)
            if data.has_key(text):
                data[text].append(adata)
            else:
                alist = [adata]
                data[text] = alist
    
    def getName(name):
        if names.has_key(name):
            return names[name]
        return name
        
    for i in range(len(gattai)):
        getGattai(gattai,i)

    for foo in data['幻魔']:
        print foo[0],foo[1]
    import simplejson
    simplejson.dump(data, open('gousei.json','w'),indent=2,ensure_ascii=False)
