from Acquisition import aq_inner
from zope.component import getMultiAdapter
from zope.interface import implements

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFPlone.browser.interfaces import ISitemapView


class VisualSitemapView(BrowserView):
    implements(ISitemapView)

    item_template = ViewPageTemplateFile('visual-sitemap-item.pt')

    def createSiteMap(self):
        context = aq_inner(self.context)
        view = getMultiAdapter((context, self.request),
                               name='sitemap_builder_view')
        data = view.siteMap()
        return self._renderLevel(children=data.get('children', []))

    def _renderLevel(self, children=[], level=2):
        output = ''
        for node in children:
            children = node.get('children', [])
            
            if len(children):
            	output += '<li class="VisualnavTreeItem withChildren">'
            else:
            	output += '<li class="VisualnavTreeItem">'
            	
            output += self.item_template(node=node)
            if len(children):
                output += \
                    '<ul class="VisualnavTreeLevel%d hidden navChild">\n%s\n</ul>\n' % (
                        level, self._renderLevel(children, level + 1))
            output += '</li>\n'

        return output
