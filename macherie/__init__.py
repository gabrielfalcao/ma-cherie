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
import os
import sys
import cherrypy

from controllers import MaCherie

def runserver(this_path):
    if not isinstance(this_path, basestring):
        raise TypeError('macherie.runserver takes a string as parameter, got None.')

    cherrypy.config.update({
        'tools.encode.on': True,
        'tools.encode.encoding': 'utf-8',
        'tools.decode.on': True,
        'tools.trailing_slash.on': True,
        'tools.staticdir.root': this_path,
        'tools.staticfile.on': True,
        'tools.staticfile.filename':"/media/img/favicon.ico",
        'view.dir': os.path.join(this_path, 'views'),
        'image.dir': os.path.join(this_path, 'data'),
        'data.dir': os.path.join(this_path, 'data'),
        'cache.dir': os.path.join(this_path, 'cache'),
    })

    cherrypy.quickstart(MaCherie(), '/', {
        '/media': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'media'
        }
    })

def main():
    if __name__ == '__main__':
        our_path = os.path.abspath(os.path.dirname(__file__))
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        runserver(our_path)


main()
