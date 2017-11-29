# -*- coding: utf-8 -*-

from plone import api

#from Products.Five import BrowserView


class StylesView():

    def call(self):
        color1 = api.portal.get_registry_record('collective.multitheme.interfaces.ICollectiveMultiThemeSettings.color1')
        color2 = api.portal.get_registry_record('collective.multitheme.interfaces.ICollectiveMultiThemeSettings.color2')
        color3 = api.portal.get_registry_record('collective.multitheme.interfaces.ICollectiveMultiThemeSettings.color3')
        return """.custom-color1 { color: #%s} .custom-color2 { color: #%s} .custom-color3 { color: #%s}
            .custom-background1 { background-color: #%s} .custom-background2 { background-color: #%s}
            .custom-background3 { background-color: #%s}""" % {color1, color2, color3, color1, color2, color3}
