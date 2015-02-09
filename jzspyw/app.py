# -*- coding: utf-8 -*-
__author__ = 'iamxi'

import web

urls = ("/.*", "index")

app = web.application(urls, globals())


class index:

    def GET(self):
        render = web.template.render('templates')
        return render.index()

if __name__ == "__main__":
    app.run