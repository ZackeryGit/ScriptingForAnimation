import maya.cmds as c
print("Hello World")

cRadius = 5
cHeight = .75
dif = 1.5
generations = 3
overlap = 1.75


height = overlap # Set to overlap in order to start above the grid
 

# Segmenets
for i in range(generations):
    sphere = c.polySphere(radius = cRadius)
    c.move(0, cRadius + height - overlap, 0, sphere)
    height += (cRadius * 2) - overlap
    cRadius -= dif
    print (height)


# Nose
nose = c.polyCone(radius = cRadius / 1, height = 4)
c.rotate(90, 0, 0 , nose, relative=True)
c.move(0, height - (cRadius + dif), (cRadius + dif), nose)

# Hat
# Base
height -= .5 #hat overlap essentiallyf
cRadius += 2
cylinder = c.polyCylinder(radius = cRadius, height = cHeight)
c.move(0, height + (cHeight / 2), 0, cylinder)
height = height + cHeight

# Top
cHeight = cHeight * 4
cRadius = cRadius * .8

cylinder = c.polyCylinder(radius = cRadius, height = cHeight)
c.move(0, height + (cHeight / 2), 0, cylinder)

