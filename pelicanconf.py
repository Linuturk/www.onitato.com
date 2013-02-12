#!/usr/bin/env python
# -*- coding: utf-8 -*- #

PLUGINS = ['pelican.plugins.gravatar',]

AUTHOR = u'Justin Phelps'
SITENAME = u"Linuturk's Natter"
SITEURL = 'http://www.onitato.com'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'
DEFAULT_PAGINATION = 10
GITHUB_URL = 'https://github.com/Linuturk/www.onitato.com'

# Blogroll
LINKS =  (('Request a Topic', 'https://github.com/Linuturk/www.onitato.com/issues'),
          ('Old Blog', 'http://linuturk.blogspot.com'),)

# Social widget
SOCIAL = (('google+', 'https://plus.google.com/112828903529889228389/posts'),
          ('github', 'https://github.com/Linuturk'),
          ('facebook', 'https://www.facebook.com/linuturk'),
          ('twitter', 'https://twitter.com/linuturk'),
          ('linkedin', 'http://www.linkedin.com/in/linuturk'),)

# static paths will be copied under the same name
STATIC_PATHS = ['images', ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),
                 ('extra/favicon.ico', 'favicon.ico'),)

# Enable pages on the menu
DISPLAY_PAGES_ON_MENU = True

# Page settings
PAGE_DIR = ('pages')
ARTICLE_EXCLUDES = (('pages',))

GOOGLE_ANALYTICS = "UA-34793085-1"
TWITTER_USERNAME = "Linuturk"
