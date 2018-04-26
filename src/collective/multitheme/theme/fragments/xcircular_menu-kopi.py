def get_items(self):
    link = self.data['linked_folder']
    folders = self.context.portal_catalog(UID=link)
    folder = folders[0]
    items =  folder.items()
    item_count = len(items)
    items = self.context.items()
    item_count = len(items)
    rotation = (2 *math.pi)/item_count
    radius = self.data['radius']
    rotate_list = []
    for index, item in enumerate(items):
        real_index = index + 1
        turner = real_index * rotation
        x = radius * math.sin(turner)
        y = radius * math.cos(turner)
        rotate_list.append({'item': item,
                            'index': index,
                            'rotation': turner,
                            'title': item[0],
                            'obj': item[1].absolute_url_path(),
                            'x':x,
                            'y':y}
        )
    return rotate_list

def get_height(self):
    radius = self.data['radius']
    return radius * 2 + 144


def get_allitems(self):
    linked = self.data['linked_folder']
    folder = self.context.portal_catalog(UID=linked)
    folder = folder[0]
    return folder.items()
    #linked_folder =  folder[0]
    #item_count = len(items)
    #items = self.context.items()
    #return folder.keys()
    #return self.context.getFolderContents(folder)
    #return linked.getFolderContents()
    #return linked.items()
    #return linked_folder.keys()
    #return linked_folder.getFolderContents()
