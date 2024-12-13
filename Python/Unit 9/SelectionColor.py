import maya.cmds as c

class Window():
    def __init__(self, title : str):
        self.title = title
        
        if c.window(self.title, exists = True):
            c.deleteUI(self.title, window = True)

        self.window = c.window(self.title, title = self.title)
        mColumn = c.columnLayout("mColumn", parent = self.window)
        c.textField(parent = mColumn, editable = 0, text="Color Index 1 - 18")
        self.colorInput = c.textField(parent = mColumn)
        c.button(
            parent=mColumn,
            label="Change Selection Color",
            command=lambda _: self.changeColor()
        )
        
    def show(self):
         c.showWindow(self.window)

    def changeColor(self):
        colorIndex = c.textField(self.colorInput, query = True, text = True)
        print(colorIndex)
        try:
            colorIndex = int(colorIndex)  # Convert to integer
        except ValueError:
            c.warning("Please enter a valid integer for the color index.")
            return

        selection = c.ls(selection=True)
        print(selection)


        for item in selection:

            shapes = c.listRelatives(item, shapes = True)
            print(shapes)
            if shapes:
                shape = shapes[0]
                c.setAttr(f"{shape}.overrideEnabled", 1)
                c.setAttr(f"{shape}.overrideColor", colorIndex)
    

            children = c.listRelatives(item, children = True)
            print(children)

            for child in children:
                    print (child)
                    shapes = c.listRelatives(child, shapes = True)
                    if shapes:
                        shape = shapes[0]
                        c.setAttr(f"{shape}.overrideEnabled", 1)
                        c.setAttr(f"{shape}.overrideColor", colorIndex)

my_window = Window(title="Selection Color")
my_window.show()
