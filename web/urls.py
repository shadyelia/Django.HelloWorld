from django.urls import re_path

from web.views import index

web_urls = [
    re_path('', index),
]
