#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'DarkRodry'
SITENAME = 'El blog de DarkRodry'
SITEURL = 'http://localhost:8000'
SITETITLE = 'Rodrigo de Frutos'
SITESUBTITLE = 'Backend Developer'
SITELOGO = "/images/avatar.jpg"
SITEDESCRIPTION = 'Aventuras y desventuras de un programador'

BROWSER_COLOR = '#333'

PATH = 'content'

# Theme stuff
THEME = "theme-flex"

# Plugins config
JINJA_ENVIRONMENT = {
  'extensions': ['jinja2.ext.i18n']
}
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

# Locale config
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'
OG_LOCALE = 'es_ES'
I18N_TEMPLATES_LANG = 'en'
LOCALE = 'es_ES.UTF-8'
DATE_FORMATS = {
    'es': '%d de %B de %Y'
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Main menu config
MAIN_MENU = True

MENUITEMS = (('Archivo', '/archives.html'),
             ('Categorias', '/categories.html'))

# Social widget
SOCIAL = (('linkedin', 'https://es.linkedin.com/in/rodrigodefrutos'),
	('github', 'https://github.com/darkrodry'),
	('twitter', 'https://twitter.com/DarkRodry'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra']

# Pigment config
PYGMENTS_STYLE = 'monokai'
