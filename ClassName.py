import sublime
import sublime_plugin
import os
import os.path

class ClassnameCopyCommand(sublime_plugin.WindowCommand):
	def run(self, paths=None):
		if paths:
			file = '*'.join(paths)
		else:
			file = sublime.active_window().active_view().file_name()
		
		if file and len(file) > 0:
			fullname = self.getClassName(file)
			if fullname:
				sublime.set_clipboard(str(fullname))
				sublime.status_message("Copied class full name: " + fullname)
			else:
				sublime.status_message("Can not find class name")

	def getClassName(self, file):
		folders = sublime.active_window().folders()
		(path, ext) = os.path.splitext(file)
		extLen = len(ext)
		for dir in folders:
			if 0 == file.find(dir):
				fullname = file[len(dir)+1:]
				if extLen > 0:
					fullname = fullname[0:-extLen]
				fullname = fullname.replace('\\', '.')
				return fullname
		
		return None



	def is_visible(self, paths=None):
		if paths:
			file = '*'.join(paths)
		else:
			file = sublime.active_window().active_view().file_name()
		return os.path.isfile(file)

