import maya.cmds as c


def sequenceRename(format: str):
    selection = c.ls(selection = True)

    formatSections = format.split("_")
    paddingAmmount = len(formatSections[1])

    count = 1
    for object in selection:

        objectNum = str(count).zfill(paddingAmmount)
        count += 1
        formatSections[1] = objectNum
        c.rename(object, "_".join(formatSections))

def sequenceRenameWindow(window):
    format = c.textField(window.format, query = True, text = True)
    selection = c.ls(selection = True)

    formatSections = format.split("_")
    paddingAmmount = len(formatSections[1])

    count = 1
    for object in selection:

        objectNum = str(count).zfill(paddingAmmount)
        count += 1
        formatSections[1] = objectNum
        c.rename(object, "_".join(formatSections))


class Window():
    def __init__(self, title : str):
        self.title = title
        
        if c.window(self.title, exists = True):
            c.deleteUI(self.title, window = True)

        self.window = c.window(self.title, title = self.title)
        mColumn = c.columnLayout("mColumn", parent = self.window)
        c.textField(parent = mColumn, editable = 0, text="Format:")
        c.textField(parent = mColumn, editable = 0, text="ObjectName_##_Type", width = 400)
        self.format = c.textField(parent = mColumn)
        c.button(
            parent=mColumn,
            label="Format",
            command=lambda _: sequenceRenameWindow(self)
        )
        
    def show(self):
         c.showWindow(self.window)

my_window = Window(title="NameFormat")
my_window.show()
