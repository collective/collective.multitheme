# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from z3c.form import interfaces
from zope import schema
from zope.interface import alsoProvides
from plone.directives import form
from medialog.iconpicker.widgets.widget import ColorPickerFieldWidget
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

#import here or from __init.py ?
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.multitheme')


class ICollectiveMultithemeLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICollectiveMultiThemeSettings(form.Schema):
	"""Adds settings to medialog.controlpanel
	"""

	form.fieldset(
		'Multitheme',
		label=_(u'Multitheme'),
		fields=[
			'style',
			'rules',
		],
	)

	style = schema.Choice(
        title=_(u"Style"),
	       values=['blue',
                    'booster',
                   'dutchblue',
                   'ploneconf',
                   'red',
                   'scheme1',
                   'spot'],
        	required=True,
    )

	color1 = schema.TextLine(
            title=_(u"Custom Color 1"),
            required=True,
    )

	color2 = schema.TextLine(
            title=_(u"Custom Color 2"),
            required=True,
    )

	color3 = schema.TextLine(
            title=_(u"Custom Color 3"),
            required=True,
    )

    form.widget(
        color1=IconPickerFieldWidget,
    )

	rules = schema.Choice(
            title=_(u"Layout Rules"),
            values=['default', 'spot'],
            required=True,
    )

alsoProvides(ICollectiveMultiThemeSettings, IMedialogControlpanelSettingsProvider)
