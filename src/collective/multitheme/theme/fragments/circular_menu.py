def get_items(self): 
    items = self.context.items()
    item_count = len(items)
    rotation = 360/item_count
    radius = self.data['radius']
    rotate_list = []
    for index, item in enumerate(items):
        turner = 90+(index*rotation)
        x = (math.cos(turner))*radius
        y = (math.sin(turner))*radius
        rotate_list.append({'item': item, 'rotation': turner, 'title': item[0], 'x':x, 'y':y})
    return rotate_list
    
    
def something(self):
    items = self.context.items()
    item_count = len(items)
    rotation = 360/(item_count)
    return item_count