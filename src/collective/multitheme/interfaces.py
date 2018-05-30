# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from medialog.iconpicker.widgets.widget import ColorPickerFieldWidget
from medialog.controlpanel.interfaces import \
    IMedialogControlpanelSettingsProvider
from plone.directives import form
from zope import schema
# import here or from __init.py ?
from zope.i18nmessageid import MessageFactory
from zope.interface import alsoProvides
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

_ = MessageFactory('collective.multitheme')


class ICollectiveMultithemeLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICollectiveMultiThemeSettings(form.Schema):
    """Adds settings to medialog.controlpanel"""

    form.fieldset(
        'Multitheme',
        label=_(u'Multitheme'),
        fields=[
            'style',
            'rules',
            'fullwidth',
            'load_css',
            'color1',
            'color2',
            'color3']
    )

    style = schema.Choice(
        title=_(u'Style'),
        values=['blue', 'booster', 'dutchblue', 'ploneconf', 'red', 'scheme1', 'spot'],
        required=True,
    )

    rules = schema.Choice(
        title=_(u"Layout Rules"),
        values=['default', 'spot', 'head'],
        required=True,
    )

    fullwidth = schema.Bool(
        title=_(u"Mosaic Full width?"),
        required=False,
    )

    load_css = schema.Bool(
        title=_(u"Load CSS? Put it in your theme and disable it here"),
        required=False,
        default=True,
    )

    color1 = schema.TextLine(
        title=_("color1", default=u"Custom Color 1"),
        required=True,
        description=_("help_color",
                      default="Choose Color"),
    )

    color2 = schema.TextLine(
        title=_("color2", default=u"Custom Color 2"),
        required=True,
        description=_("help_color",
                      default="Choose Color"),
    )

    color3 = schema.TextLine(
        title=_("color3", default=u"Custom Color 3"),
        required=True,
        description=_("help_color",
                      default="Choose Color"),
    )

    form.widget(
        color1=ColorPickerFieldWidget,
        color2=ColorPickerFieldWidget,
        color3=ColorPickerFieldWidget,
    )


alsoProvides(ICollectiveMultiThemeSettings, IMedialogControlpanelSettingsProvider)
