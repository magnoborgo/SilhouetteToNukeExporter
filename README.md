# SilhouetteToNukeExporter
This script exports selected shapes as Nuke Roto Shapes to a folder


##  Usage:

Put the script inside Silhouette's "/scripts/actions/" folder

Add the shortcut on your sfxuser.py file:

path = "/path/to/your/temp/export/folder/" 
fx.bind('F10', callMethod(fx.actions["ExportNukeShapes"].execute, path))





