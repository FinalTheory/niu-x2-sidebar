#!/usr/bin/env python
# -*- coding: utf-8 -*- #

###################################################################################################



from __future__ import unicode_literals
from markdown.extensions import headerid, codehilite
from collections import OrderedDict
import datetime
import md5
import os

###################################################################################################
# 系统的全局设置

# 名称以及站点相关
AUTHOR = u'FinalTheory'
SITENAME = u'FinalTheory\u7684\u6280\u672f\u611f\u609f'
HOMENAME = u'首页'
# HOMEURL = ''
SITEURL = ''

# 时间与区域
DEFAULT_LANG = u'zh_CN'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE = 'fs'
UPDATEDATE_MODE = 'metadata'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

###################################################################################################
# 与路径相关的设置，以及插件等

PATH = 'content'
STATIC_PATHS = ['images', 'files', 'extra']
THEME = "MyTheme/pelican-theme"
PLUGIN_PATHS = ['pelican-plugins', 'MyTheme']
FILENAME_METADATA = '(?P<slug>.*)'
PLUGINS = [
    'assets',
    'gravatar',
    'extract_headings',
    'niux2_hermit_player',
    'niux2_lazyload_helper',
    'pelican-update-date',
    'sitemap',
    'summary',
    'render_math',
]

# 下面这个dict定义了一组编译后不变的静态地址链接
# 注意这里路径的写法，如果是在Linux下，要换成对应的风格！
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/LICENSE.txt': {'path': 'LICENSE.txt'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

TEMPLATE_PAGES = {
		"abstracts.html": "abstracts.html",
    "404.html": "404.html",
    "archives_updatedate.html": "archives_updatedate.html",
}

# 下面这组设置重新安排了article输出、page输出以及目录、标签的布局方式
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'

# disable author pages
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

###################################################################################################
# RSS以及文章输出相关的设置

# 缓存策略与页面输出
SUMMARY_MAX_LENGTH = 10
MAX_ABSTRACT_NUM = 3
LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False
# 加入这个傻逼插件后，会在包含大写的header中自动加入<span>，因此一定要关掉！！！
TYPOGRIFY = False

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = None
FEED_MAX_ITEMS = 20
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 文章分类的设置
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_CATEGORY = 'uncategorized'
DEFAULT_PAGINATION = 8


# 其他高级设置
READERS = {
    'html': None,
}

###################################################################################################
# 插件高级设置

JINJA_EXTENSIONS = ['jinja2.ext.ExprStmtExtension',]

# sitemap plugin config
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


# extrac_headings plugin config
def my_slugify(value, sep):
    if type(value) == unicode:
        # Fix for encoding errors
        if 'nt' in os.name.lower():
            value = value.encode('gb18030')
        else:
            value = value.encode('utf-8')
    m = md5.new()
    m.update(value)
    return m.digest().encode('hex')[:5]
MY_SLUGIFY_FUNC = my_slugify
MY_HEADING_LIST_STYLE = 'ol'


# niux2_lazyload_helper plugin config
def my_img_url_2_path(url):
    header = 'lazy:'
    if not url.startswith(header):
        print("ignore " + url)
        return '', url
    return os.path.abspath(os.path.join('content', url[1 + url.index('/', len(header)):])), url[len(header):]
MY_IMG_URL2PATH_FUNC = my_img_url_2_path


MD_EXTENSIONS = ([
    'nl2br',
    'extra',
    'footnotes',
    'tables',
    codehilite.CodeHiliteExtension(configs=[('linenums', False), ('guess_lang', False)]),
    headerid.HeaderIdExtension(configs=[('slugify', my_slugify)]),
])


###################################################################################################
# 设置主题中的中文翻译
NIUX2_AUTHOR_TRANSL = '作者'
NIUX2_404_TITLE_TRANSL = '404错误'
NIUX2_404_INFO_TRANSL = '请求的页面未找到！'
NIUX2_TAG_TRANSL = '标签'
NIUX2_ARCHIVE_TRANSL = '归档'
NIUX2_ARCHIVE_UPDATEDATE_TRANSL = '归档（按修改时间）'
NIUX2_CATEGORY_TRANSL = '分类'
NIUX2_TAG_CLEAR_TRANSL = '清空'
NIUX2_TAG_FILTER_TRANSL = '过滤标签'
NIUX2_HEADER_TOC_TRANSL = '目录'
NIUX2_SEARCH_TRANSL = '搜索'
NIUX2_SEARCH_PLACEHOLDER_TRANSL = 'Google需要翻墙哦亲~'
NIUX2_COMMENTS_TRANSL = '评论'
NIUX2_PUBLISHED_TRANSL = '发布时间'
NIUX2_LASTMOD_TRANSL = '最后修改'
NIUX2_PAGE_TITLE_TRANSL = '页面'
NIUX2_RECENT_UPDATE_TRANSL = '最近修改'
NIUX2_HIDE_SIDEBAR_TRANSL = '隐藏侧边栏'
NIUX2_SHOW_SIDEBAR_TRANSL = '显示侧边栏'
NIUX2_REVISION_HISTORY_TRANSL = '修订历史'
NIUX2_VIEW_SOURCE_TRANSL = '查看源文件'
NIUX2_LAZY_LOAD_TEXT = '囧rz~努力加载中！'

# 其他与主题相关的设置

NIUX2_AUTHOR_LINK = SITEURL
NIUX2_PYGMENTS_THEME = 'github'
NIUX2_PAGINATOR_LENGTH = 11
NIUX2_RECENT_UPDATE_NUM = 10
NIUX2_FAVICON_URL = '/favicon.ico'
NIUX2_GOOGLE_CSE_ID = '017413529027733437042:wvv9ghano_a'
NIUX2_DISPLAY_TITLE = True
NIUX2_LAZY_LOAD = True
NIUX2_TOOLBAR = True
# 这个选项是用来显示博客的提交历史的，如果是托管在github上面的话
# NIUX2_GITHUB_REPO = ''

NIUX2_CATEGORY_MAP = {
    'algorithm': ('算法', 'fa-cogs'),
    'research': ('研究', 'fa-flask'),
    'note': ('笔记', 'fa-book'),
    'life': ('日常', 'fa-coffee'),
    'thinking': ('随笔', 'fa-leaf'),
    'collection': ('收藏', 'fa-briefcase'),
}

NIUX2_HEADER_SECTIONS = [
    ('标签', 'Tags', '/tag/', 'fa-tags'),
    ('项目', 'My Projects', '/MyProjects.html', 'fa-rocket'),
    ('关于我', 'About Me', '/AboutMe.html', 'fa-anchor'),
    ('网站首页', 'Site HomePage', 'http://finaltheory.me/', 'fa-sitemap'),
]

NIUX2_HEADER_DROPDOWN_SECTIONS = OrderedDict()
NIUX2_HEADER_DROPDOWN_SECTIONS[('归档', 'fa-archive')] = [
    ('归档 (按发布时间)', 'archives order by publish time', '/archives.html', 'fa-calendar'),
    ('归档 (按修改时间)', 'archives order by modify time', '/archives_updatedate.html', 'fa-pencil'),
]

NIUX2_FOOTER_LINKS = [
    ('LICENSE', 'Terms, license and privacy etc', '/LICENSE.txt', ''),
]

NIUX2_FOOTER_ICONS = [
    ('fa-wordpress', 'My WordPress Blog', 'http://wp.finaltheory.me'),
    ('fa-github', 'My Github Page', 'https://github.com/FinalTheory'),
    ('fa-cloud', 'My CodeForces Page', 'http://codeforces.com/profile/FinalTheory'),
    ('fa-renren', 'My RenRen Page', 'http://renren.com/FinalTheory'),
    ('fa-facebook-square', 'My Facebook Page', 'https://www.facebook.com/ForFinalTheory'),
    ('fa-envelope-o', 'Send E-mail to Me', 'mailto: FinalTheory@hotmail.com'),
    ('fa-rss', 'Subscribe My Blog', '/feed.xml'),
]
