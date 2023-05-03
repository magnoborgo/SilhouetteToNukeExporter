# SilhouetteToNukeExporter
This script exports selected Shapes (and Trackers update:May 2023) as Nuke project file into a specified folder

##  Usage:

Put the script inside Silhouette's "/scripts/actions/" folder

Add the shortcut on your sfxuser.py file:

path = "/path/to/your/temp/export/folder/" </br>
fx.bind('F10', callMethod(fx.actions["ExportNukeShapes"].execute, path))





