#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wsgiref.handlers, cgi, logging, os ,time, urllib

from google.appengine.ext import webapp,db
from google.appengine.ext.webapp import template
from django.utils import simplejson

import search

class MainPage(webapp.RequestHandler):

    def _get_results(self,detail):
        results = {
            'detail':detail,
            'all_devils':search.devil_list,
            }
        if not detail:
            results['index'] = True
            return results
        #デモニカもどき
        if detail['name'] == u'デモニカもどき':
            results['password_only'] = True
            results['demonica_modoki'] = search.demonica_modoki_data
            return results
        
        #パスワード限定悪魔
        if search.is_password_only(detail):
            results['password_only'] = True
            return results
        
        #狂神合体時 
        if search.search_kyoshin(detail):
            results['kyoshin'] = True
            return results
        
        #特殊合体時 
        special_result = search.search_special(detail)
        if special_result:
            results['special'] = special_result
            return results

        #精霊だった時
        normal_results = search.search_element(detail)
        if normal_results:
            results['normals'] = normal_results
            return results

        #御霊だった時
        normal_results = search.search_mitama(detail)
        if normal_results:
            results['normals'] = normal_results
            return results
        
        normal_results = search.search_converter(detail)
        #コンバータ使用
        if normal_results:
            results['normals'] = normal_results
            results['converter'] = True
            return results
        
        #普通の検索
        normal_results = search.search_normal(detail)
        min_max = search.get_min_max(detail)
        elements = search.search_element_up(detail)
        results['normals'] = normal_results
        results['min_max'] = min_max
        results['elements'] = elements
        return results

    def get(self,name):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        detail = None
        if name:
            name = urllib.unquote_plus(name)
            name = unicode(name,'utf-8')
            logging.debug(name)
            detail = search.detail_data.get(name)
        if name and not detail:
            self.response.out.write('404 Daemon Not Found.')
            self.response.set_status(404)
            return

        values = self._get_results(detail)
        self.response.out.write(template.render(path, values))

    def post(self,*name):
        name = self.request.get("name")
        self.redirect('/' + urllib.quote_plus(name.encode('utf-8')))

def main():
    application = webapp.WSGIApplication(
        [(r'/(.*)',MainPage),
         ],
        debug=True)
    logging.getLogger().setLevel(logging.DEBUG)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
