#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'DarkRodry'
SITENAME = 'DarkRodry\'s Blog'
SITEURL = 'http://localhost:8000'
SITETITLE = 'Rodrigo de Frutos'
SITESUBTITLE = 'Backend Developer'
SITELOGO = "/images/avatar.jpg"
SITEDESCRIPTION = 'aprendiz de scala-escritor novato'

BROWSER_COLOR = '#333'

PATH = 'content'

# Theme stuff
THEME = "theme-flex"

# Locale config
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'es'

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

STATIC_PATHS = ['images', 'extra/CNAME']

# Pigment config
PYGMENTS_STYLE = 'native'
