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
        results = {}
        if detail:
            results = search.get_results(name)
        logging.debug(detail)
        logging.debug(results)
        values = {
            'detail':detail,
            'results' : results,
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
