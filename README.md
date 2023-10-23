# Maya Python module & plugin template

A template to quickly make a Python plugin & module for Maya

### Instructions
- click 🟩`use this template` to create your GitHub repo, & clone it
- Module setup 
  - rename the `MyModule` folder & `MyModule/myModule.mod` 
  - open the `.mod` file and change the module name inside
- Plugin setup
  - rename the demo plugin `MyModule/plug-ins/hello_world.py` 
  - add load & unload code to the `initializePlugin` & `uninitializePlugin` methods
  - optionally handle command registration on load & unload 
- add your Python modules to `MyModule/scripts`
- Optional
  - replace this `README.md` with your own instructions
  - Add a LICENSE
  - delete all `.gitkeep` files
  - add a button or menu entry that opens the documentation url

### Module

A module let's you change the Maya environment, without changing your Maya installation.  
e.g. add resources, plugins, environment paths, ...  
We use this to register our plugin with Maya in a modular way: When the user registers the module, everything else is automatically hooked up.  

- the MyModule directory contains the module files.
- the icons, plug-ins, presets, and scripts subdirectories are the default directories that Maya expects to find in a module. You can choose to use different directories or multiple directories in your module, but you will need to specify these in the (.mod) module description file.
  - Add any icons used in your add-on to the icons directory
  - Add C++ and Python plug-ins to the plug-ins directory
  - Add presets to the presets directory
  - Add any MEL or Python scripts to the scripts directory
- Create a module description file file with the `.mod` extension (see [docs](https://help.autodesk.com/view/MAYAUL/2023/ENU/?guid=Maya_SDK_Distributing_Maya_Plug_ins_DistributingUsingModules_ModuleDescriptionFiles_html))

### Plugin
Plugins let the user easily enable / disable a tool in Maya (with Maya's plugin manager)  
They also let you run code on startup, without editing the `userSetup.py` file, keeping your Maya clean / vanilla.  

![](https://www.sidefx.com/media/uploads/products/engine/hengine_maya_load.jpg)  
This project includes a `hello_world.py` plugin (a demo plugin from the Maya docs).  
Plugins should be placed in the `MyModule/plug-ins` folder
- note that `initializePlugin` & `uninitializePlugin` methods don't follow the PEP8 name convention. Do not change this.

### Scripts
Python modules become importable when placed in `myModule/scripts`.  
It might be a good practice to develop them in a separate repo, so the module can have it's own `pyproject.toml` & `requirements.txt`

### Icons
Icons in the icon folder can be accessed in Qt by name:
```python
# search custom icons in the maya icon path. only default maya icons are exposed to qt.
def get_icon_path(name: str = None) -> Optional[str]:
    default_name = "cube.png"
    name = name or default_name
    for icon_dir in os.environ.get('XBMLANGPATH', '').split(os.pathsep):
        icon_path = os.path.join(icon_dir, name)
        if os.path.exists(icon_path):
            return icon_path
    if name != default_name:
        return get_icon_path(default_name)

icon = QtGui.QIcon(QtGui.QPixmap(':/trash.png'))
```

### presets
attribute presets
- [ ] TODO createa a sample  
[docs](https://help.autodesk.com/view/MAYAUL/2023/ENU/?guid=GUID-B90EF3C9-EFB8-4BBC-B9A5-69F7EC86B3C3)

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
- [module layout docs](https://help.autodesk.com/view/MAYAUL/2023/ENU/?guid=Maya_SDK_Distributing_Maya_Plug_ins_DistributingUsingModules_CreatingAModulePackage_html)
- [module install docs](https://help.autodesk.com/view/MAYAUL/2023/ENU/?guid=Maya_SDK_Distributing_Maya_Plug_ins_DistributingUsingModules_InstallingModules_html)
  - you can manually install the module by moving the MyModule folder in the maya modules folder 
  - maya searches for modules in the `MAYA_MODULE_PATH` env var
  - you can also add paths to `Maya.env` file
- [maya plugin docs](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_A_First_Plugin_Python_html)
