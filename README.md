# Django 博客小项目

##版本：

Django 1.10.5

Python 3.6.0

##项目：

目前实现博客列表页、文章页、评论区及提交新评论。

CSS、js 等文件是用的 Bootstrap 源码，借用了一个样式，对前端的 CSS 等不是十分熟悉。

##设置

LANGUAGE_CODE = 'zh-Hans' #en-us

TIME_ZONE = 'Asia/Shanghai'

DATEBASES 增加"TIME_ZONE : 'Asia/Shanghai'"

STATICFIES_DIRS = [os.path.join(BASE_DIR, 'static')]

##功能

自制一个 filter，使用 markdown 模块，让博客文章体和评论体支持 markdown 编辑
