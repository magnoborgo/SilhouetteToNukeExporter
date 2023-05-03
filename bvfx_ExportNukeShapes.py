# Boundary Visual Effects - Export Nuke Shapes
# Version 1.0
#
# For greeting, bugs, and requests email me at mborgo[at]boundaryvfx.com
# Compatibility: Silhouette v4.2.1 and up, not tested in previous versions
#
# If you like it and use it frequently, please consider a small donation to the author,
# via Paypal on the email mborgo[at]boundaryvfx.com

#===============================================================================
# This action will export the selected shapes to a previously setup folder with 1 click
#===============================================================================

#===============================================================================
# Version Log
# v1 (2013/05/06)
#===============================================================================

# Copyright (c) 2012-2013, Magno Borgo    
# All rights reserved.
#
# BSD-style license:
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Magno Borgo or its contributors may be used to
#        endorse or promote products derived from this software without
#        specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
#PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
#BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
#OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
#OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
#EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


#===============================================================================
# Instructions to use
#
# ****Attention: you need to setup a save path on the script ******
# that can be done on sfxuser.py or here on the script.
# if you want to hardcode the path on the script, edit the path="/path/to/folder" part of the code near the end of this file:
#
# or add the following code to the sfxuser.py to use it with a keyboard shortcut:
'''
def callMethod(func, *args, **kwargs):
    def _return_func():
        return func(*args, **kwargs)

path = "/your/desired/save/path/"
fx.bind('F10', callMethod(fx.actions["ExportNukeShapes"].execute, path))

#or use something like this

fx.bind('F10', callMethod(fx.actions["ExportNukeShapes"].execute,"/savepath/in/the/disk"))
''' 
#===============================================================================


from fx import *
from tools.objectIterator import getObjects
import os

def doExport(self, path):
	sel = selection()
	if len(sel) == 0:
		status("Select some shapes before trying to export!")
	else:	
		if not os.path.exists(path):
			print("\nWARNING\n**************\nExportNukeShapes Script: The path does not exists, set it correctly on the script")
		
		path = os.path.abspath(path)
	
		# get the "Nuke 6.2+" module	
		module = io_modules["Nuke 6.2+ Shapes"]
		shapes = getObjects(selection(), types=[Shape])
		if len(shapes) > 0:
			self.counter += 1
			name = "sfx_shapes" + str(self.counter)
			ext = ".nk"
			shapePath = os.path.join(path, name + ext)
			module.export(shapePath)
			status("Nuke 6.2+ Shapes exported to " + path)

		module = io_modules["Nuke 5"]
		trackers = getObjects(selection(), types=[Tracker])
		if len(trackers) > 0:

			self.counter += 1
			name = "sfx_trackers" + str(self.counter)
			ext = ".nk"
			shapePath = os.path.join(path, name + ext)
			module.export(shapePath)
			status("Nuke 6.2+ Trackers exported to " + path)
		
		if len(shapes) > 0 and len(trackers) > 0:
			status("Nuke 6.2+ Shapes and Trackers exported to " + path)
	

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