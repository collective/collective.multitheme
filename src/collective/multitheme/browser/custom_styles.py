# -*- coding: utf-8 -*-

from plone import api

#from Products.Five import BrowserView


class StylesView(self):

    def call(self):
        return """<style>.custom-color1 {color: red} </style>"""

    def color1(self):
        return api.portal.get_registry_record('collective.multitheme.interfaces.ICollectiveMultiThemeSettings.color1')

    def color2(self):
        return api.portal.get_registry_record('collective.multitheme.interfaces.ICollectiveMultiThemeSettings.color2')

    def color3(self):
        return api.portal.get_registry_record('collective.multitheme.interfaces.ICollectiveMultiThemeSettings.color3')
