def item_url(self):
    item = load_item(self)
    return item.getURL()

def load_item(self):
    item =  self.data['content_item']
    items =self.context.portal_catalog(UID=item)
    return items[0]