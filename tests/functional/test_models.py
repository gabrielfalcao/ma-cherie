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
import cherrypy
from macherie import models
from utils import assert_raises

templates = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
data = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))

def test_filesystem_can_access():
    assert models.FileSystem.can_access('/etc/') == True, \
           'Current user should have permission to access /etc/'

def test_filesystem_can_modify():
    assert models.FileSystem.can_modify('/etc/') == False, \
           'Current user should not have permission to modify /etc/'

def test_filesystem_list_images():
    expected_files = [
        'file.jpg',
        'file.JPG',
        'file.JPg',
        'file.jPg',
        'file.gif',
        'file.png',
        'file.jpeg',
    ]
    expected_paths = sorted([os.path.join(templates, f) for f in expected_files])

    for fname in expected_paths:
        open(fname, 'w').write('Fake img file')

    got_paths = models.FileSystem.list_images(templates)

    try:
        assert got_paths == expected_paths, "Expected %r, got %r" % (got_paths, expected_paths)
    finally:
        for f in expected_paths:
            os.remove(f)

def test_file_all():
    cherrypy.config['data.dir'] = data
    files = models.File.all()

    assert isinstance(files, list), 'models.File.all() should ' \
           'return a list, got %r' % files
    assert len(files) == 2, 'models.File.all() looking for ' \
           'images on "%s" should return 2 images. Got %d' \
           % (data, len(files))

    condition = isinstance(files[0], models.File) and isinstance(files[1], models.File)
    assert condition, 'the files returned by models.File.all() ' \
           'should be instances of models.File. Got %r' % files
