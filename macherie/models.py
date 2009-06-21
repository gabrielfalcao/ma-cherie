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

class File(object):
    pass

class Folder(object):
    pass

class FileSystem(object):
    @classmethod
    def has_permission(self, path):
        perms = os.F_OK|os.W_OK|os.R_OK|os.X_OK
        return os.access(path, perms)

class FileHandler(object):
    base_path = None
    file_system = None

    def __init__(self, path, file_system=FileSystem):
        if not isinstance(path, basestring):
            raise TypeError('FileHandler.path should be string, got %r' % path)

        self.base_path = unicode(path)
        self.file_system = file_system
