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

import cherrypy
from macherie import views
from utils import assert_raises

def test_views_has_make_url_function():
    assert hasattr(views, 'make_url'), 'macherie.views should have the function make_url'
    assert callable(views.make_url), 'macherie.views.make_url should be callable'

def test_make_url_takes_string_as_param():
    expected = r'macherie.views.make_url ' \
               'takes a string as param, got None.'
    assert_raises(TypeError, views.make_url, None, exc_pattern=expected)

def test_make_url_without_trailling_slash():
    base_url = 'http://my.unit.test/for/ma-cherie'
    cherrypy.request.base = base_url

    expected_url = 'http://my.unit.test/for/ma-cherie/index'
    got_url = views.make_url('index')
    assert got_url == expected_url, 'Expected %s, got %s' % (expected_url, got_url)

def test_make_url_with_trailling_slash_on_base_url():
    base_url = 'http://my.unit.test/for/ma-cherie/'
    cherrypy.request.base = base_url

    expected_url = 'http://my.unit.test/for/ma-cherie/index'
    got_url = views.make_url('index')
    assert got_url == expected_url, 'Expected %s, got %s' % (expected_url, got_url)

def test_make_url_with_trailling_slash_on_url_part():
    base_url = 'http://my.unit.test/for/ma-cherie'
    cherrypy.request.base = base_url

    expected_url = 'http://my.unit.test/for/ma-cherie/index'
    got_url = views.make_url('/index')
    assert got_url == expected_url, 'Expected %s, got %s' % (expected_url, got_url)

def test_make_url_with_trailling_slash_on_both():
    base_url = 'http://my.unit.test/for/ma-cherie/'
    cherrypy.request.base = base_url

    expected_url = 'http://my.unit.test/for/ma-cherie/index'
    got_url = views.make_url('/index')
    assert got_url == expected_url, 'Expected %s, got %s' % (expected_url, got_url)

def test_views_has_function_render_html():
    assert hasattr(views, 'render_html'), 'macherie.views should have the function render_html'
    assert callable(views.render_html), 'macherie.views.render_html should be callable'

def test_views_has_function_jpeg():
    assert hasattr(views, 'jpeg'), 'macherie.views should have the function jpeg'
    assert callable(views.jpeg), 'macherie.views.jpeg should be callable'

