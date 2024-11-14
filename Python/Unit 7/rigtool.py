import maya.cmds as c
selection = c.ls(selection=True)
print(selection)
for item in selection:
    group = c.group(empty = True, name = item + "_Grp")
    # Get Attributes
    translation = c.xform(item, query = True, translation=True)
    rotation = c.xform(item, query = True, rotation=True)
    # Set Attributes
    c.xform(group, translation = translation)
    c.xform(group, rotation = rotation)
    c.parent(item, group)
    # Freeze Transforms
    c.makeIdentity(item, scale=True, translate=True, rotate=True, normal=True)
