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

from macherie import helpers
from utils import assert_raises

def test_has_file_class():
    assert hasattr(helpers, 'File'), \
           'macherie.helpers does not have the class File'
    assert issubclass(helpers.File, object), \
           'macherie.helpers.File is not a class. ' \
           'Got %r instead' % helpers.File

def test_has_folder_class():
    assert hasattr(helpers, 'Folder'), \
           'macherie.helpers does not have the class Folder'
    assert issubclass(helpers.Folder, object), \
           'macherie.helpers.Folder is not a class. ' \
           'Got %r instead' % helpers.Folder

def test_has_filesystem_class():
    assert hasattr(helpers, 'FileSystem'), \
           'macherie.helpers does not have the class FileSystem'
    assert issubclass(helpers.Folder, object), \
           'macherie.helpers.FileSystem is not a class. ' \
           'Got %r instead' % helpers.Folder

def test_has_filehandler_class():
    assert hasattr(helpers, 'FileHandler'), \
           'macherie.helpers does not have the class FileHandler'
    assert issubclass(helpers.FileHandler, object), \
           'macherie.helpers.FileHandler ' \
           'is not a class. Got %r instead' % helpers.FileHandler

class TestFileSystem:
    def test_filesystem_has_method_has_permission(self):
        msg1 = 'FileSystem.has_permission does not exist'
        msg2 = 'FileSystem.has_permission is not a method'
        assert hasattr(helpers.FileSystem, 'has_permission'), msg1
        assert callable(helpers.FileSystem.has_permission), msg2

class TestFileHandler:
    def test_file_handler_construction_fails_without_parameters(self):
        assert_raises(TypeError,
                      helpers.FileHandler,
                      exc_pattern=r'__init__.. takes at least 2 arguments .1 given.')

    def test_file_handler_construction_fails_with_more_than_two_parameters(self):
        assert_raises(TypeError,
                      helpers.FileHandler,
                      None,
                      None,
                      None,
                      exc_pattern=r'__init__.. takes at most 3 arguments .4 given.')

    def test_file_handler_construction_fails_with_non_string_param(self):
        assert_raises(TypeError,
                      helpers.FileHandler,
                      None,
                      exc_pattern=r'FileHandler.path should be string, got None')

    def test_filehandler_takes_a_string_at_construction(self):
        assert isinstance(helpers.FileHandler('/home'), helpers.FileHandler)

    def test_filehandler_has_base_path_attr(self):
        handler = helpers.FileHandler('/home/kept')
        msg = "helpers.FileHandler('/home/kept') should have attribute base_path"
        assert hasattr(handler, 'base_path'), msg

    def test_filehandler_holds_its_string_in_base_path_attribute(self):
        path = '/home/kept'
        handler = helpers.FileHandler(path)
        msg = "helpers.FileHandler('/home/kept').base_path should be %r, but is %r"
        assert handler.base_path == path, msg % (path, handler.base_path)

    def test_filehandler_holds_base_path_as_unicode(self):
        path = '/home/kept'
        handler = helpers.FileHandler(path)
        msg = "helpers.FileHandler('/home/kept').base_path " \
              "should be type unicode, but is %r"
        assert isinstance(handler.base_path, unicode), msg % (type(handler.base_path))

    def test_filehandler_has_file_system_attr(self):
        handler = helpers.FileHandler('/home/foo')
        msg = "helpers.FileHandler('/home/foo') should have attribute file_system"
        assert hasattr(handler, 'file_system'), msg

    def test_filehandler_construction_with_custom_file_system(self):
        class FileSystemStub:
            pass

        handler = helpers.FileHandler('/home/foo', file_system=FileSystemStub)
        assert isinstance(handler, helpers.FileHandler)

    def test_filehandler_construction_with_custom_file_system_holds_attr(self):
        class FileSystemStub:
            pass

        handler = helpers.FileHandler('/home/fs/bar', file_system=FileSystemStub)
        msg = "helpers.FileHandler('/home/foo').file_system " \
              "be %r, but is %r"

        assert handler.file_system is FileSystemStub, \
               msg % (FileSystemStub, handler.file_system)
