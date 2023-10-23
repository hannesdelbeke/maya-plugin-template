import sys
import maya.api.OpenMaya as om


def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass


# command
class Py2HelloWorldCmd(om.MPxCommand):
    kPluginCmdName = "py2HelloWorld"

    def __init__(self):
        om.MPxCommand.__init__(self)

    @staticmethod
    def cmdCreator():
        return Py2HelloWorldCmd()

    def doIt(self, args):
        print ("Hello World!")


# Initialize the plug-in
def initializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.registerCommand(
            Py2HelloWorldCmd.kPluginCmdName, Py2HelloWorldCmd.cmdCreator
        )
    except:
        sys.stderr.write(
            "Failed to register command: %s\n" % Py2HelloWorldCmd.kPluginCmdName
        )
    raise


# Uninitialize the plug-in
def uninitializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.deregisterCommand(Py2HelloWorldCmd.kPluginCmdName)
    except:
        sys.stderr.write(
            "Failed to unregister command: %s\n" % Py2HelloWorldCmd.kPluginCmdName
        )
    raise
    
