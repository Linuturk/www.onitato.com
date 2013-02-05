#!/usr/bin/env python
# -*- coding: utf-8 -*- #

PLUGINS = ['pelican.plugins.gravatar',]

AUTHOR = u'Justin Phelps'
SITENAME = u"Linuturk's Natter"
SITEURL = 'http://www.onitato.com'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'
GITHUB_URL = 'https://github.com/Linuturk/www.onitato.com'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('google+', 'https://plus.google.com/112828903529889228389/posts'),
          ('github', 'https://github.com/Linuturk'),
          ('facebook', 'https://www.facebook.com/linuturk'),
          ('twitter', 'https://twitter.com/linuturk'),
          ('youtube', 'http://www.youtube.com/user/Linuturk'),
          ('linkedin', 'http://www.linkedin.com/in/linuturk'),)

DEFAULT_PAGINATION = 10

# static paths will be copied under the same name
STATIC_PATHS = ["images", ]
