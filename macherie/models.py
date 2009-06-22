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
import glob
import cherrypy
import Image

class File(object):
    def __init__(self, path):
        self.path = path
        self.name = os.path.split(path)[1]
        self.img = Image.open(path)
        self.width = self.img.size[0]
        self.height = self.img.size[1]

    @classmethod
    def all(cls):
        return [cls(f) for f in FileSystem.list_images(cherrypy.config['data.dir'])]

class Folder(object):
    pass

class FileSystem(object):
    @classmethod
    def can_modify(self, path):
        perms = os.F_OK|os.W_OK|os.R_OK|os.X_OK
        return os.access(path, perms)

    @classmethod
    def can_access(self, path):
        perms = os.F_OK|os.R_OK|os.X_OK
        return os.access(path, perms)

    @classmethod
    def list_images(self, path):
        lst = []
        for filename in os.listdir(path):
            if filename.lower().endswith('.jpg') or \
               filename.lower().endswith('.jpeg') or \
               filename.lower().endswith('.gif') or \
               filename.lower().endswith('.png'):
                lst.append(os.path.join(path, filename))

        return sorted(lst)

class FileHandler(object):
    base_path = None
    file_system = None

    def __init__(self, path, file_system=FileSystem):
        if not isinstance(path, basestring):
            raise TypeError('FileHandler.path should be string, got %r' % path)

        self.base_path = unicode(path)
        self.file_system = file_system
