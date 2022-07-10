#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'DarkRodry'
SITENAME = 'El blog de DarkRodry'
SITEURL = 'http://localhost:8000'
SITETITLE = 'Rodrigo de Frutos'
SITESUBTITLE = 'Miscelaneous Developer'
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
PLUGINS = [
  'i18n_subsites',
  'minchin.pelican.plugins.nojekyll',
  'post_stats',
]

# Locale config
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'
OG_LOCALE = 'es_ES'
I18N_TEMPLATES_LANG = 'es'
LOCALE = ('es_ES.UTF-8')
DATE_FORMATS = {
    'es': '%d de %B de %Y'
}

# Integrations
DISQUS_SITENAME = 'darkrodry-github-blog'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Main menu config
MAIN_MENU = True

DISABLE_URL_HASH = True

MENUITEMS = (('Archivo', '/archives.html'),
             ('Categorias', '/categories.html'))

# Social widget
SOCIAL = (('linkedin', 'https://es.linkedin.com/in/rodrigodefrutos'),
	('github', 'https://github.com/darkrodry'),
	('twitter', 'https://twitter.com/DarkRodry'))

# Default configs
DEFAULT_PAGINATION = 10
DEFAULT_METADATA = {
    'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'slides']

# Pigment config
MARKDOWN = {
  'extension_configs': {
      'markdown.extensions.codehilite': {
        'css_class': 'highlight',
        'pygments_style': 'dracula',
        'noclasses': True,
        'guess_lang': True,
      },
      'markdown.extensions.extra': {},
      'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}


