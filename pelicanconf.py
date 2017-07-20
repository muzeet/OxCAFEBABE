#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import math

JINJA_FILTERS = {
    'count_to_font_size': lambda c: '{p:.1f}%'.format(p=100 + 25 * math.log(c, 2)),
}

AUTHOR = u'muzeet'
SITENAME = u"OxCAFEBABE"
SITEURL = 'http://www.muzeet.com'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'


DEFAULT_LANG = u'zh'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

#THEME_STATIC_PATHS = ['static']


# 日期格式
DATE_FORMAT = {
	 'cn':('zh_CN','%Y-%m-%d, %a'),
}


# Feed generation is usually not desired when developing

# Blogroll

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
		)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


DUOSHUO_SITENAME = "muzeet"
THEME = "themes/Responsive-Pelican"
THEME_STATIC_DIR = 'theme'



#让categories不显示在menu中
DISPLAY_CATEGORIES_ON_MENU = False
#让pages不显示在menu中
DISPLAY_PAGES_ON_MENU = False
#菜单项
MENUITEMS = ((u"博客主页","/"),
			 (u"文章列表","/archives.html"),
             (u"分类目录","/categories.html"),
			 (u"Cloud&Data","/category/Cloud&Data/"),
			 (u"程序人生","/category/Code/"),
			 (u"读书","/category/读书/"),
			 (u"博客设计","/category/博客设计/"),
			 (u"关于本站","#"),
            )
#文章显示
ARTICLE_URL='posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS='posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
#使用模板中的哪些模板
DIRECT_TEMPLATES = ['index', 'categories', 'archives']

#文章安装年月归档
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'
#DAY_ARCHIVE_SAVE_AS =  'posts/archive/{date:%Y}/{date:%b}/{data:%d}/index.html'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images']
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

#Category显示
CATEGORY_URL='category/{name}/'
CATEGORY_SAVE_AS='category/{name}/index.html'
#标签格式Tag
TAG_URL='tag/{name}/'
TAG_SAVE_AS='tag/{name}/index.html'
#tag cloud 标签云
TAG_CLOUD_STEPS=4
TAG_CLOUD_MAX_ITEMS=100

#代码注释
PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}

'''
from markdown.extensions import codehilite
MD_EXTENSIONS = ([
    'extra',
    'footnotes',
    'tables',
    codehilite.CodeHiliteExtension(configs=[('linenums', true), ('guess_lang', False)]),
])
'''

#将静态文件拷贝到output目录下
#FILES_TO_COPY = (
#    ("extra/sitelogo.ico", "sitelogo.ico"),
#)

