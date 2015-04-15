#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'iamxi'

import cherrypy
from lib.tool.template import MakoLoader

main = MakoLoader()
cherrypy.tools.mako = cherrypy.Tool('on_start_resource', main)

from jzspyw.app import Index
cherrypy.config.update('conf/server.cfg')
cherrypy.tree.mount(Index(), '/', 'conf/jzspyw.cfg')
cherrypy.engine.start()
cherrypy.engine.block()