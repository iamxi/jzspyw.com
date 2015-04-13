# -*- coding: utf-8 -*-
__author__ = 'iamxi'

import cherrypy


class Index:

    @cherrypy.expose
    def index(self):
        return 'hello'