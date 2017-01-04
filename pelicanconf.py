#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'DarkRodry'
SITENAME = 'DarkRodry\'s Blog'
SITEURL = 'https://darkrodry.github.io/'
SITETITLE = 'Rodrigo de Frutos'
SITESUBTITLE = 'Backend Developer'
SITEDESCRIPTION = 'aprendiz de scala-escritor novato'

PATH = 'content'

# Locale config
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/DarkRodry'),
	('linkedin', 'https://es.linkedin.com/in/rodrigodefrutos'),
	('github', 'https://github.com/darkrodry'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']

# Theme stuff
THEME = "theme-flex"

BIO = "Desarrollador backend, aprendiz de Scala, escritor novato"
SITELOGO = "/images/avatar.jpg"
