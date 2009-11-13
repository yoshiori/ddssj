#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import simplejson
except:
    from django.utils import simplejson
import os

skill_data = simplejson.load(open(os.path.join(os.path.dirname(__file__), 'data/skill_detail.json')))

def search(name):
    return skill_data.get(name)
