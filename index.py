#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wsgiref.handlers, cgi, logging, os ,time, urllib

from google.appengine.ext import webapp,db
from google.appengine.ext.webapp import template
from django.utils import simplejson

import search

class MainPage(webapp.RequestHandler):

    def get(self,name):
        name = urllib.unquote_plus(name)
        name = unicode(name,'utf-8')
        logging.debug(name)
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        detail = []
        if name:
            detail = search.detail_data[name]
        nomal_results = {}
        special_result = []
        if detail:
            special_result = search.search_special(detail)
            if not special_result :
                nomal_results = search.search_nomal(detail)
        logging.debug(detail)
        logging.debug(nomal_results)
        values = {
            'detail':detail,
            'nomal' : nomal_results,
            'special' : special_result,
            }

        self.response.out.write(template.render(path, values))

    def post(self,*name):
        name = self.request.get("name")
#        print name.encode('utf-8')
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