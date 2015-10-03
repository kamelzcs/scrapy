#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 zhao <zhao@kamel-ThinkPad-X201>
#
# Distributed under terms of the MIT license.
# Refer http://scrapy.org/

import scrapy
import json


class MySpider(scrapy.Spider):
    name = 'github'
    start_urls = ['https://api.github.com/users/kamelzcs/repos']
    def parse(self, response):
         jsonresponse = json.loads(response.body_as_unicode())
         print [_['name'] for _ in jsonresponse]
         return
