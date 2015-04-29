# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class MathRip(Item):
    name = Field()
    school = Field()
    year = Field()
    url = Field()
