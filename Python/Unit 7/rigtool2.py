import maya.cmds as c

selection = c.ls(selection=True)
print(selection)



for item in selection:

    # Name Formatting
    name = item
    print(name)
    if (name.find("_") != -1):
        print("part")
        name = name.rpartition("_")[0]
        parent = c.listRelatives(item, parent = True)[0]

    # Get Attributes from item
    translation = c.xform(item, query = True, translation=True, worldSpace = True)
    rotation = c.xform(item, query = True, rotation=True, worldSpace = True)


    # Get Bigger Scale X or Z
    groupZ = c.xform(item, query = True, scale = True)[2]
    groupX = c.xform(item, query = True, scale = True)[0]

    groupSize = 0

    if (groupZ > groupX):
        groupSize = groupZ
    else:
        groupSize = groupX 


    # Create Control
    print(groupSize)
    control = c.circle(radius = groupSize, name = name + "_Ctrl")
    ctrlGroup = c.group(empty = True, name = name + "Ctrl_Grp", parent = item)
    c.xform(control, translation = translation)
    rotation[2] += 90
    c.xform(control, rotation = rotation)
    
    c.parent(control, ctrlGroup)