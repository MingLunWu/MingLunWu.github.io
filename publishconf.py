#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os 

AUTHOR = 'MingLun Wu'
SITENAME = "MingLun's Blog"
SITEURL = 'https://minglunwu.github.io'

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

PLUGIN_PATHS = ['./plugins']
PLUGINS = ["ga_page_view", "extended_sitemap"]

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


STATIC_PATHS = ["images", "extra"]
# HOMEPAGE_URL = "https://minglunwu.github.io"
HOMEPAGE_URL = "https://minglunwu.com"
STATIC_FOLDER = HOMEPAGE_URL + "/theme"

EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"}
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
GOOGLE_ANALYTICS = 'UA-161863471-1'
GOOGLE_SERVICE_ACCOUNT = 'minglunwu@personal-blog-278509.iam.gserviceaccount.com'
GOOGLE_KEY_FILE = './personal-blog-278509-1601b8241698.json'
GA_START_DATE = '2020-05-01'
GA_END_DATE = 'today'
GA_METRIC = 'ga:pageviews'
POPULAR_POST_START = 'A month ago'

# sitemap
EXTENDED_SITEMAP_PLUGIN = {
    'priorities': {
        'index': 1.0,
        'articles': 0.8,
        'pages': 0.5,
        'others': 0.4
    },
    'changefrequencies': {
        'index': 'daily',
        'articles': 'weekly',
        'pages': 'monthly',
        'others': 'monthly',
    }
}

# DISQUS
DISQUS_SITENAME = 'minglunwu'

""" from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = ''
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = "" """
# GOOGLE_ANALYTICS = 'UA-161863471-1'
