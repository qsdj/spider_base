# -*- coding: utf-8 -*-
import js2py
import scrapy
import requests



class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['sse.com.cn']
    start_urls = ['http://www.sse.com.cn/assortment/stock/list/share/']

    def parse(self, response):
        # 创建js的执行环境
        context = js2py.EvalJs()

        js_url = 'http://static.sse.com.cn/js/lib/jquery.min.js'

        # 获取js对应的响应
        response = requests.get(js_url)
        js = response.content.decode()

        # context.execute(js)
        # js2py.eval_js(js)

        # print(js2py.eval_js(js))
