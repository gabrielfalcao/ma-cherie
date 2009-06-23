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
import Image
import ImageDraw
import cherrypy
import StringIO

from genshi.template import TemplateLoader

base_path = os.path.join(os.path.dirname(__file__), '..', 'data')

def make_url(url):
    if not isinstance(url, basestring):
        raise TypeError('macherie.views.make_url ' \
                        'takes a string as param, got %r.' % url)
    if url.startswith('/'):
        url = url[1:]

    base = cherrypy.request.base
    if base.endswith('/'):
        base = base[:-1]

    return "%s/%s" % (base, url)

def render_html(filename, context, template_path=None):
    if not isinstance(filename, basestring):
        raise TypeError('macherie.views.render_html ' \
                        'takes a string as filename param, got %r.' % filename)

    if not len(filename):
        raise TypeError('macherie.views.render_html ' \
                        'filename param can not be empty.')

    if not isinstance(context, dict):
        raise TypeError('macherie.views.render_html ' \
                        'takes a dict as context param, got %r.' % context)

    if 'make_url' in context.keys():
        msg = 'The key "make_url" is already in ' \
              'template context as: %r' % context['make_url']
        raise KeyError(msg)

    if template_path is None:
        try:
            template_path = cherrypy.config['views.dir']
        except KeyError:
            raise LookupError('You must configure "views.dir" string in ' \
                              'CherryPy or pass template_path param to render_html')


    elif not isinstance(template_path, basestring):
        raise TypeError('macherie.views.render_html ' \
                        'takes a string as template_path param, got %r.' % template_path)

    context['make_url'] = make_url
    loader = TemplateLoader(template_path,
                            auto_reload=True)
    template = loader.load(filename)
    generator = template.generate(**context)
    return generator.render('html', doctype='html')



def jpeg(path, base_path=base_path, img_module=Image, stringio_module=StringIO):
    if not isinstance(path, basestring):
        raise TypeError('jpeg() takes a string as parameter, got %r.' % path)
    fullpath = os.path.join(base_path, path)
    try:
        img = img_module.open(fullpath)
    except IOError, e:
        cherrypy.response.status = 404
        return unicode(e)

    sfile = stringio_module.StringIO()
    img.save(sfile, "JPEG", quality=100)
    cherrypy.response.headers['Content-type'] = "image/jpeg"
    return sfile.getvalue()

def picture(img,
            width,
            height,
            field='image',
            crop=False,
            center=True,
            must_cache=True,
            mask=None,
            background=0xffffff):

    width, height = int(width), int(height)
    wished_size = width, height
    img = Image.open(getattr(picture, field).path)

    if crop:
        img = fit(img, (width, height))

    if center:
        old_img = img
        img = Image.new('RGBA', (width, height), background)
        ow, oh = old_img.size
        left = (width - ow) / 2
        top = (height - oh) / 2
        img.paste(old_img, (left, top))

    if mask:
        mask_img = Image.open(mask)
        img.paste(mask_img, None, mask_img)

    return jpeg_response(img)
