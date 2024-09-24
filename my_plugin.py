import sys
import maya.api.OpenMaya as om
import maya.cmds as cmds
import maya.mel as mel


# this plugin menu setup creates a single menu entry
# to create a menu under Windows/my-tool

# The below sample will create a new menu and menu-item: ToolsMenu/My cool tool
# MENU_NAME is the name maya assigns to a menu, this is not always the same as the visible label
# e.g. to parent to the default Maya menu 'Windows', use MENU_NAME="mainWindowMenu"
MENU_NAME = "ToolsMenu"  # no spaces in names, use CamelCase. Used to find and parent to a menu.
MENU_LABEL = "Tools"  # spaces are allowed in labels, only used when we create a new menu
MENU_ENTRY_LABEL = "My cool tool"

MENU_PARENT = "MayaWindow"  # do not change

__menu_entry_name = "" # Store generated menu item, used when unregister


def maya_useNewAPI():  # noqa
    """dummy method to tell Maya this plugin uses the Maya Python API 2.0"""
    pass


# # =============================== Command ===========================================
# class HelloWorldCommand(om.MPxCommand):
#     command_name = "HelloWorld"
#
#     # def __init__(self):
#     #     om.MPxCommand.__init__(self)
#
#     # @staticmethod
#     # def command_creator():
#     #     return HelloWorldCommand()
#
#     def doIt(self, args):
#         print("Hello World!")
#
#
# def register_command(plugin):
#     pluginFn = om.MFnPlugin(plugin)
#     try:
#         pluginFn.registerCommand(HelloWorldCommand.command_name, HelloWorldCommand.__init__)
#     except Exception as e:
#         sys.stderr.write(f"Failed to register command: {HelloWorldCommand.command_name}\n")
#         raise e
#
#
# def unregister_command(plugin):
#     pluginFn = om.MFnPlugin(plugin)
#     try:
#         pluginFn.deregisterCommand(HelloWorldCommand.command_name)
#     except Exception as e:
#         sys.stderr.write(f"Failed to unregister command: {HelloWorldCommand.command_name}\n")
#         raise e


# =============================== Menu ===========================================
def show(*args):
    """this command is run when clicked in the Maya menu, replace it with your own code"""
    # import your custom module here, instead of at the top of the python file.
    # to always enable Maya to activate your plugin & create the menu, even if there are compile errors in your code.
    # it also means no code will run untill the user clicks the menu, a good practice to keep Maya startup fast.
    # often you create your Qt Widget here and then show it.
    print("hello")


def loadMenu():
    """Setup the Maya menu, runs on plugin enable"""
    global __menu_entry_name

    # Maya builds its menus dynamically upon being accessed, so they don't exist if not yet accessed.
    # We force a menu build to allow parenting any new menu under a default Maya menu
    mel.eval("evalDeferred buildFileMenu")  # delete this if not parenting menus to a default Maya Menu

    if not cmds.menu(f"{MENU_PARENT}|{MENU_NAME}", exists=True):
        cmds.menu(MENU_NAME, label=MENU_LABEL, parent=MENU_PARENT)
    __menu_entry_name = cmds.menuItem(label=MENU_ENTRY_LABEL, command=show, parent=MENU_NAME)


def unloadMenuItem():
    """Remove the created Maya menu entry, runs on plugin disable"""
    if cmds.menu(f"{MENU_PARENT}|{MENU_NAME}", exists=True):
        menu_long_name = f"{MENU_PARENT}|{MENU_NAME}"
        # Check if the menu item exists; if it does, delete it
        if cmds.menuItem(__menu_entry_name, exists=True):
            cmds.deleteUI(__menu_entry_name, menuItem=True)
        # Check if the menu is now empty; if it is, delete the menu
        if not cmds.menu(menu_long_name, query=True, itemArray=True):
            cmds.deleteUI(menu_long_name, menu=True)


# =============================== Plugin (un)load ===========================================
def initializePlugin(plugin):
    """Code to run when the Maya plugin is enabled, this can be manual or during Maya startup"""
    # register_command(plugin)
    loadMenu()


def uninitializePlugin(plugin):
    """Code to run when the Maya plugin is disabled."""
    # to allow the user to enable and disable your plugin on the fly without any issues
    # anything created or setup during initializePlugin should be cleaned up in this method.
    # however if you don't, a user can instead disable the plugin & then restart Maya.

    # unregister_command(plugin)
    unloadMenuItem()
    
