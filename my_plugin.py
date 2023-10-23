import sys
import maya.api.OpenMaya as om
import maya.cmds as cmds


MENU_NAME = "ToolsMenu"  # no spaces in names, use CamelCase
MENU_LABEL = "Tools"  # spaces are fine in labels
MENU_ENTRY_LABEL = "My cool tool"

MENU_PARENT = "MayaWindow"  # do not change

def maya_useNewAPI():  # noqa
    pass  # dummy method to tell Maya this plugin uses Maya Python API 2.0


# =============================== Command ===========================================
class HelloWorldCommand(om.MPxCommand):
    command_name = "HelloWorld"

    # def __init__(self):
    #     om.MPxCommand.__init__(self)

    # @staticmethod
    # def command_creator():
    #     return HelloWorldCommand()

    def doIt(self, args):
        print ("Hello World!")


def register_command(plugin):
    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.registerCommand(HelloWorldCommand.command_name, HelloWorldCommand.__init__)
    except Exception as e:
        sys.stderr.write(f"Failed to register command: {HelloWorldCommand.command_name}\n")
        raise e
  

def unregister_command(plugin):
    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.deregisterCommand(HelloWorldCommand.command_name)
    except Exception as e:
        sys.stderr.write(f"Failed to unregister command: {HelloWorldCommand.command_name}\n")
        raise e


# =============================== Menu ===========================================
def show(*args):
    # TODO import our custom module
    print("hello")


def loadMenu():
    if not cmds.menu(MENU_NAME, exists=True):
        cmds.menu(MENU_NAME, label=MENU_LABEL, parent=MENU_PARENT)
    cmds.menuItem(label=MENU_ENTRY_LABEL, command=show)  # , parent=MENU_NAME)  


def unloadMenuItem():
    if cmds.menu(MENU_NAME, exists=True):
        menu_item_long_name = MENU_NAME + "|" + MENU_ENTRY_LABEL
        # Check if the menu item exists; if it does, delete it
        if cmds.menuItem(menu_item_long_name, exists=True):
            cmds.deleteUI(menu_item_long_name, menuItem=True)
        # Check if the menu is now empty; if it is, delete the menu
        if not cmds.menu(MENU_NAME, query=True, itemArray=True):
            cmds.deleteUI(MENU_NAME, menu=True)


# =============================== Plugin (un)load ===========================================
def initializePlugin(plugin):
    register_command(plugin)
    loadMenu()


def uninitializePlugin(plugin):
    unregister_command(plugin)
    unloadMenuItem()
    
