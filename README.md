# Maya Python plugin template

A template to quickly make a Python plugin for Maya. (For modules, see [Maya module template](https://github.com/hannesdelbeke/maya-module-template))

### Features
- a `pyproject.toml` to support pip install
- Maya menu sample code

### Instructions
- click 🟩`use this template` to create your GitHub repo, & clone it
- change the data in the `pyproject.toml`
- add dependencies to both `requirements.txt` and `pyproject.toml`
- Plugin setup
  - rename the demo plugin folder
  - add load & unload code to the `initializePlugin` & `uninitializePlugin` methods
  - optionally handle command registration on load & unload 
- Optional
  - replace this `README.md` with your own instructions
  - Add a LICENSE

### Plugin
Plugins let the user easily enable / disable a tool in Maya (with Maya's plugin manager)  
They also let you run code on startup, without editing the `userSetup.py` file, keeping your Maya clean / vanilla.  

![](https://www.sidefx.com/media/uploads/products/engine/hengine_maya_load.jpg)  
This project includes a `hello_world.py` plugin (a demo plugin from the Maya docs).  
Plugins should be placed in the `MyModule/plug-ins` folder
- note that `initializePlugin` & `uninitializePlugin` methods don't follow the PEP8 name convention. Do not change this.

### installation
TODO
### menu entry
- [ ] Create the menu on the plugin initialize
- [ ] **TODO replace with cmds code, pymel is not included by default anymore**
```python
import pymel.core as pm
main_maya_window = pm.language.melGlobals['gMainWindow'] 
custom_menu = pm.menu('Custom Menu', parent=main_maya_window)
pm.menuItem(label="hello", command="print('hello')", parent=custom_menu)
```
- [ ] unload the menu on uninitialize
- You can also use [unimenu](https://github.com/hannesdelbeke/unimenu) to add your tool to the Maya menu. Recommended for studio setups  

TODO
### tool entry
TODO
### shelf entry
TODO

### Command

Adding a command to your plugin is optional. (I never had the need for it)
In Maya Python scripting, MPxCommand is a base class for creating custom commands. Below is a simple example of creating a custom command using MPxCommand. This example demonstrates a command that creates a cube.

```python
import maya.api.OpenMaya as om
import maya.cmds as cmds

class CreateCubeCommand(om.MPxCommand):
    commandName = "createCube"

    def __init__(self):
        super(CreateCubeCommand, self).__init__()

    def doIt(self, args):
        # Parse the arguments if needed (not used in this example)

        # Create a cube
        cube = cmds.polyCube()[0]

        # Set the result to the name of the created cube
        self.setResult(cube)

# Creator function
def createCubeCommand():
    return om.asMPxPtr(CreateCubeCommand())

# Initialize the plugin
def initializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.registerCommand(
            CreateCubeCommand.commandName,
            createCubeCommand
        )
    except:
        om.MGlobal.displayError(
            "Failed to register command: {}".format(
                CreateCubeCommand.commandName
            )
        )

# Uninitialize the plugin
def uninitializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.deregisterCommand(CreateCubeCommand.commandName)
    except:
        om.MGlobal.displayError(
            "Failed to unregister command: {}".format(
                CreateCubeCommand.commandName
            )
        )

# Usage:
# 1. Save this script as "createCubeCmd.py"
# 2. Load the script in Maya using the following commands:
#    ```
#    import maya.cmds as cmds
#    cmds.loadPlugin("path/to/createCubeCmd.py")
#    ```
# 3. Run the custom command:
#    ```
#    cmds.createCube()
#    ```
```

### references
- [maya plugin docs](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_A_First_Plugin_Python_html)