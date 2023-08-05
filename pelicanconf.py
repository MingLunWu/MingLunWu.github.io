#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os 

AUTHOR = 'MingLun Wu'
SITENAME = "MingLun's Blog"
SITEURL = ''

PATH = 'content'
ARTICLE_PATH = ["notes"]
ARTICLE_SAVE_AS = 'notes/{date:%Y}/{slug}.html'
ARTICLE_URL = 'notes/{date:%Y}/{slug}.html'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'en_US'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


STATIC_PATHS = ["images"]
HOMEPAGE_URL = "https://minglunwu.github.io"
STATIC_FOLDER = HOMEPAGE_URL + "/theme"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

GOOGLE_SERVICE_ACCOUNT = "minglunwu@personal-blog-278509.iam.gserviceaccount.com"
GOOGLE_KEY_FILE = "./personal-blog-278509-1601b8241698.json"
GA_START_DATE = "2020-01-01"
GA_END_DATE = "today"

# GOOGLE_ANALYTICS = 'UA-161863471-1'
GOOGLE_ANALYTICS = "G-NC508K3RBY"

DISQUS_SITENAME = 'minglunwu'



