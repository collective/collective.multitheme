def get_items(self):
    linked = self.data['linked_folder']
    folder = self.context.portal_catalog(UID=linked)
    items = folder[0].getObject().items()
    item_count = len(items)
    rotation = (2 *math.pi)/item_count
    radius = self.data['radius']
    rotate_list = []
    for index, item in enumerate(items):
        real_index = index + 1
        turner = real_index * rotation
        x = radius * math.sin(turner)
        y = radius * math.cos(turner)
        item1 = item[1]
        rotate_list.append({'item': item,
                            'index': index,
                            'rotation': turner,
                            'title': item[0],
                            'obj': item1.absolute_url_path(),
                            'x':x,
                            'y':y,
                            'iconfield': item1.iconfield}
        )
    return rotate_list

def get_height(self):
    radius = self.data['radius']
    return radius * 2 + 144


def get_allitems(self):
    linked = self.data['linked_folder']
    folder = self.context.portal_catalog(UID=linked)
    #items =  plone.api.content.find(context=folder)
    return folder[0].getObject().items()
     #.contentItems()
    #return folder.keys()       # Plone 4 or newer
    #return folder[0]
    #linked_folder =  folder[0]
    #items = self.context.items()
    #return folder.keys()
    #return self.context.getFolderContents(folder)
    #return linked.getFolderContents()
    #return linked.items()
    #return linked_folder.keys()
    #return linked_folder.getFolderContents()
