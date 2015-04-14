#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'iamxi'

import cherrypy
import jzspyw.app

cherrypy.config.update('conf/server.cfg')
cherrypy.tree.mount(jzspyw.app.Index(), '/', 'conf/jzspyw.cfg')
cherrypy.engine.start()
cherrypy.engine.block()