from fx import *
from tools.objectIterator import getObjects
import os

def doExport(self, path):

	sel = selection()
	if len(sel) == 0:
		status("Select some shapes before trying to export!")
	else:
		if not os.path.exists(path):
			print "\nWARNING\n**************\nExportNukeShapes Script: The path does not exists, set it correctly on the script"

		path = os.path.abspath(path)

		# get the "Nuke 6.2+" module
		module = io_modules["Nuke 6.2+ Shapes"]
		shapes = getObjects(selection(), types=[Shape])
		self.counter += 1
		name = "sfx_shapes" + str(self.counter)#"s.label
		ext = ".nk"
		shapePath = os.path.join(path, name + ext)
		module.export(shapePath)
		status("Nuke 6.2+ Shapes exported to " + path)




class ExportNukeShapes(Action):
	"""Export nuke shapes automation"""

	def __init__(self):
		Action.__init__(self, "BoundaryVFX|Export Nuke Shapes Automation")
		self.counter = 0
		self.path = "/path/to/folder"

	def available(self):
		assert len(selection()) > 0, "Select one or more shapes or Layers"

	def execute(self, path="/path/to/folder"):
		doExport(self, path)

addAction(ExportNukeShapes())