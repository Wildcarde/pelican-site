#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Garrett McGrath'
SITENAME = 'Less Typing, More Goofing'
SITESUBTITLE = 'Internet Wanderings and Sysadmin Shlock'
SITEURL = 'blog.shadowgears.com'


PATH = 'content'

TIMEZONE = 'America/New_York'
THEME = '/home/gmcgrath/workingarea/libs/pelican-themes/pelican-bootstrap3'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# Blogroll
LINKS = (('Giantbomb', 'http://www.giantbomb.com/news/'),
         ('C++ ISO', 'https://isocpp.org/blog'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    }


STATIC_PATHS = [
    'resources',
    'extra/robots.txt',
    ]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
PLUGIN_PATHS = ['/home/gmcgrath/workingarea/libs/pelican-plugins/',
                '/home/gmcgrath/envs/pelican/lib/python3.3/site-packages/']
PLUGINS = ['pelican_gist', 'optimize_images',
        'liquid_tags.img', 'liquid_tags.video',
        'liquid_tags.youtube', 'liquid_tags.vimeo',
        'liquid_tags.include_code', 'liquid_tags.notebook']
ARTICLE_PATHS = ['2012','2011','2010','2009','2008','2015']

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']

#pelican-boostrap3 confs
DISPLAY_CATEGORIES_ON_MENU = 0

DISPLAY_ARTICLE_INFO_ON_INDEX = 1

ABOUT_ME = 'ABOUT ME Text.'
AVATAR = 'resources/site/bigavatar.jpg'


# Social widget
SOCIAL = (('github', 'https://github.com/Wildcarde'),
          ('linkedin', 'http://www.linkedin.com/in/gmcgrath'),
          ('twitter', 'https://twitter.com/Wildcarde815'),
          )

DISPLAY_CATEGORIES_ON_SIDEBAR = 1
DISPLAY_RECENT_POSTS_ON_SIDEBAR = 1
DISPLAY_TAGS_ON_SIDEBAR = 0
DISPLAY_TAGS_INLINE = 1
