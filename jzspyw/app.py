# -*- coding: utf-8 -*-
__author__ = 'iamxi'

import cherrypy


class Index:

    @cherrypy.expose
    @cherrypy.tools.mako(filename="index.html")
    def index(self):
        return ''