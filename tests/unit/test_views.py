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
from pmock import *

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

def test_jpeg_takes_path_as_param():
    assert_raises(TypeError, views.jpeg, exc_pattern=r'jpeg.. takes at least 1 argument .0 given.')

def test_jpeg_param_should_be_string():
    assert_raises(TypeError, views.jpeg, None, exc_pattern=r'jpeg.. takes a string as parameter, got None.')

def test_jpeg_success():
    path = '/path/to/mocked/img.jpg'
    img_mock = Mock()
    pil_mock = Mock()
    stringio_module_mock = Mock()
    stringio_mock = Mock()
    return_mock = Mock()

    stringio_mock.expects(once()).getvalue().will(return_value(return_mock))

    stringio_module_mock.expects(once()).StringIO().will(return_value(stringio_mock))

    pil_mock.expects(once()).open(eq(path)).will(return_value(img_mock))

    img_mock.expects(once()).save(eq(stringio_mock), eq("JPEG"), quality=eq(100))
    return_got = views.jpeg(path, img_module=pil_mock, stringio_module=stringio_module_mock)

    pil_mock.verify()
    stringio_module_mock.verify()
    img_mock.verify()
    stringio_mock.verify()
    assert return_got == return_mock, 'The return of views.jpeg() should be %r, got %r' % (return_mock, return_got)
    mime = cherrypy.response.headers['Content-type']
    assert mime == 'image/jpeg', 'The response header "Content-type" should be image/jpeg, but got %r' % mime

