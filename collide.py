def collide(obj1, obj2):

    #LEFT
    if obj1.x + obj1.width < obj2.x:
        return False
    #TOP
    if obj1.y + obj1.height < obj2.y:
        return False
    #RIGHT
    if obj1.x > obj2.x + obj2.width:
        return False
    #BOTTOM
    if obj1.y > obj2.y + obj2.height:
        return False
    return True
