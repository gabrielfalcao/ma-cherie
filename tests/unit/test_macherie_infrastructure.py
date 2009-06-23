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

import macherie

from utils import assert_raises
from pmock import *

def test_runserver_takes_string_as_parameter():
    assert_raises(TypeError, macherie.runserver, None, exc_pattern=r'macherie.runserver takes a string as parameter, got None.')

def test_main_runner():
    old_runserver = macherie.runserver
    class os(object):
        class path(object):
            @classmethod
            def abspath(*args, **kw):
                return '/absolute/path'
            @classmethod
            def dirname(*args, **kw):
                return 'dir name'
            @classmethod
            def join(*args, **kw):
                return '/joint/path'

    class sys(object):
        class path(object):
            @classmethod
            def append(*args, **kw):
                pass


    infra_mock = Mock()
    infra_mock.expects(once()).runserver(eq('/absolute/path'))

    macherie.runserver = infra_mock.runserver
    macherie.os = os
    macherie.sys = sys
    macherie.__name__ = '__main__'

    macherie.main()

    infra_mock.verify()
    macherie.__name__ = 'macherie.__init__'
