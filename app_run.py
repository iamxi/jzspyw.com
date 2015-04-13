#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'iamxi'

import cherrypy
import jzspyw.app

cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.quickstart(jzspyw.app.Index())