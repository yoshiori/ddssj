#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson
if __name__ == '__main__':
    status_data = simplejson.load(open('status.json'))
    devil_list  = simplejson.load(open('skill.json'))
    
    list = {}
    for line in devil_list:
        status = status_data[line[2]]
        del status[3]
        del status[2]
        line += status
        line[0] = int(line[0])
        list[line[2]] = line
        #        print line

        file = open('devil_detail.json','w')
        file.write(
        simplejson.dumps(list,
                    indent=2,ensure_ascii=False).encode('utf-8')
            )
        file.close()
