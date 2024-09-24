# Maya Python plugin template

A template to quickly make a Python plugin for Maya. (For modules, see [Maya module template](https://github.com/hannesdelbeke/maya-module-template)  

## Features

When installed, Maya's plug-in manager displays your plugin  
![image](https://github.com/hannesdelbeke/maya-plugin-template/assets/3758308/a7134b7c-e9a0-45a9-8853-3493e191e848)  
With the plug-in manager you can :
- easily enable / disable a tool in Maya
- Auto run code on startup, without editing your `userSetup.py` file, keeping your Maya clean / vanilla. (great for debugging)

#### handle dependencies automatically
A pip install auto handles dependencies, removing the need for vendoring dependencies. Without pip install you need to manually install the dependencies.  
This template includes a `pyproject.toml` to support a pip install to a Maya plugin folder, this command triggers a pip install from this repo:
```
pip install https://github.com/hannesdelbeke/maya-plugin-template/archive/refs/heads/main.zip --target "C:/Users/%username%/Documents/Maya/plug-ins"
```
<details>
<summary>Read this if the above command fails</summary>

<sup>_1. if the target folder doesn't exist, this command creates a `Maya/plug-ins` folder in your documents , which requires admin access._</sup>  
<sup>_2. When a user has been renamed on Windows, `%username%` will return the current name. But the folder path will use the old name, resulting in this demo command failing._</sup>  
</details>
Maya plugins don't support Python packages, they only support a single `.py` file.  
To include a package in your plugin, I recommend to use pip dependencies.

### menu entry
- Create a menu when the plugin is enabled
- Unload the menu on plugin unload

> PS: You can also use [unimenu](https://github.com/hannesdelbeke/unimenu) to add your tool to the Maya menu. Recommended for more advanced - and less modular - studio setups.

## Instructions
- click 🟩`use this template` to create your GitHub repo, & clone it
- change the data in the `pyproject.toml`
- add dependencies to both `requirements.txt` and `pyproject.toml`
- Plugin setup
  - rename the demo plugin folder
  - add load & unload code to the `initializePlugin` & `uninitializePlugin` methods
      - `initializePlugin` & `uninitializePlugin` don't follow the PEP8 name convention. Do not change this, or they won't run.
  - optionally handle command registration on load & unload 
- Optional
  - replace this `README.md` with your own instructions
  - Add a LICENSE


### installation
- [ ] TODO


### Extras
<details>
<summary>see command info</summary>

You can add commands to you Maya plugin. Included this in the template but I never use this. Feel free to just delete all code related to commands.

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
</details>
<br>

might consider adding
- [ ] toolbox entry
- [ ] shelf entry

<details>
<summary>sample repos using this template</summary>

create a PR to add your repo below 😊
- https://github.com/hannesdelbeke/maya-pip-qt
- https://github.com/plugget/plugget-qt-maya-plugin
- https://github.com/hannesdelbeke/pyblish-maya-plugin
- https://github.com/hannesdelbeke/maya-plugin-duplicate-obj-along-curve
- https://github.com/hannesdelbeke/maya-plugin-snap-to-closest-UV

</details>

### references
- [maya plugin docs](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_A_First_Plugin_Python_html)
- list loaded plugins, find plugin command from plugin, .. docs https://download.autodesk.com/us/maya/2010help/CommandsPython/pluginInfo.html#flagcommand
- similar maya plugin template https://github.com/minoue/miMayaPlugins/blob/master/plugin_templates/python_command/pyPluginCmd.py

