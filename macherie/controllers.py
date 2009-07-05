#!/usr/bin/env python
# -*- coding: utf-8; -*-
#
# Copyright (C) 2009 Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
import re
import Image
import cherrypy

from macherie.models import File
from sponge.view import render_html, jpeg, picture
from sponge.controller import ImageHandler

class MaCherie(object):
    image = ImageHandler(should_cache=True)

    @cherrypy.expose
    def index(self, **kw):
        title = u'Ma Cherie'
        content = 'Picture navigator'
        images = File.all()
        if 'search' in kw.keys():
            images = [i for i in images if kw['search'].lower() in i.name.lower()]

        return render_html('index.html', dict(title=title, content=content, images=images))
